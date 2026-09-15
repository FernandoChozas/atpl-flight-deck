const CACHE_NAME = 'atpl-flightdeck-v1.0';
const STATIC_ASSETS = [
  './',
  './index.html',
  './data.js',
  './data.json',
  './apple-touch-icon-180x180.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // External APIs (ntfy telemetry, live METAR, etc.) bypass cache
  if (url.origin !== location.origin) {
    return;
  }

  // Local assets: Cache-First with Network Fallback
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        fetch(event.request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, networkResponse);
            });
          }
        }).catch(() => {});
        return cachedResponse;
      }

      return fetch(event.request).then((networkResponse) => {
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }
        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });
        return networkResponse;
      }).catch(() => {
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html');
        }
      });
    })
  );
});

self.addEventListener('message', (event) => {
  if (event.data && event.data.action === 'CACHE_URLS') {
    const urlsToCache = event.data.urls || [];
    caches.open(CACHE_NAME).then((cache) => {
      return Promise.all(
        urlsToCache.map((u) => {
          return fetch(u).then((res) => {
            if (res.ok) return cache.put(u, res);
          }).catch(() => {});
        })
      );
    }).then(() => {
      if (event.source && event.source.postMessage) {
        event.source.postMessage({ action: 'CACHE_URLS_COMPLETE', success: true });
      }
    });
  }
});

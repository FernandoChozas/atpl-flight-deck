const CACHE_NAME = 'atpl-flightdeck-v1.4.1';
const STATIC_ASSETS = [
  './',
  './index.html',
  './data.js',
  './data.json',
  './apple-touch-icon-180x180.png',
  './world_aviation_logo.png'
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

  // External APIs (ntfy telemetry, live METAR, Open-Meteo, etc.) bypass cache
  if (url.origin !== location.origin) {
    return;
  }

  // HTML Navigation: Network-First with Cache Fallback (guarantees latest version on load)
  if (event.request.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname.endsWith('/')) {
    event.respondWith(
      fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const responseToCache = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseToCache);
            });
          }
          return networkResponse;
        })
        .catch(() => {
          return caches.match(event.request).then((cached) => {
            return cached || caches.match('./index.html');
          });
        })
    );
    return;
  }

  // Local static assets: Cache-First with background revalidation
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
      });
    })
  );
});

self.addEventListener('message', (event) => {
  if (event.data) {
    if (event.data.action === 'SKIP_WAITING') {
      self.skipWaiting();
    } else if (event.data.action === 'CACHE_URLS') {
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
  }
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
      for (const client of clientList) {
        if ('focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow('./');
      }
    })
  );
});

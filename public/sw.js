// Fri3d 2026 gezinsplanner — offline shell.
// Bewust tolerant: als één bestand ontbreekt mag de installatie niet stukgaan,
// want dan wordt de service worker nooit actief en is de app niet installeerbaar.
const CACHE = 'fri3d2026-v6';
const SHELL = [
  './', './manifest.json', './kaart.png',
  './icon-192.png', './icon-512.png', './icon.svg',
  './shiftedmake-logo.png', './fri3d-logo.png',
  './fonts/space-grotesk-700.woff2', './fonts/inter-var.woff2'
];

self.addEventListener('install', e => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await Promise.all(SHELL.map(u => c.add(u).catch(() => {})));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  if (new URL(req.url).origin !== self.location.origin) return; // Supabase en fri3d.be nooit cachen

  e.respondWith((async () => {
    try {
      const res = await fetch(req);
      if (res && res.ok) {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(req, copy)).catch(() => {});
      }
      return res;
    } catch (err) {
      const hit = await caches.match(req);
      if (hit) return hit;
      if (req.mode === 'navigate') {
        const shell = await caches.match('./');
        if (shell) return shell;
      }
      throw err;
    }
  })());
});

// Tik op een melding: breng de bestaande app naar voren in plaats van
// een tweede venster te openen.
self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil((async () => {
    const all = await self.clients.matchAll({ type: 'window', includeUncontrolled: true });
    for (const c of all) {
      if (c.url.startsWith(self.location.origin)) return c.focus();
    }
    return self.clients.openWindow('./');
  })());
});

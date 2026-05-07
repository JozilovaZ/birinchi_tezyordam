const CACHE_NAME = 'tez-yordam-v1';
const urlsToCache = [
    '/',
    '/static/loyiha/css/style.css',
    '/static/loyiha/js/main.js',
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(urlsToCache))
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                if (response) return response;
                return fetch(event.request)
                    .then(res => {
                        if (!res || res.status !== 200) return res;
                        const responseClone = res.clone();
                        caches.open(CACHE_NAME)
                            .then(cache => cache.put(event.request, responseClone));
                        return res;
                    });
            })
    );
});

var galleryFeed = new Instafeed({
    get: "user",
    userId: 7084318071,
    accessToken: "7084318071.1677ed0.1c82ce11157e4041af30c9b1c9acb55e",
    resolution: "thumbnail",
    useHttp: "true",
    limit: 6,
    template: '<div class="col-4"><a href="{{link}}"><div class="img-featured-container"><div class="img-backdrop"></div><div class="description-container"><p class="caption">{{caption}}</p><span class="likes"><i class="icon ion-heart"></i> {{likes}}</span><span class="comments"><i class="icon ion-chatbubble"></i> {{comments}}</span></div><img src="{{image}}" class="img-responsive"></div></a></div>',
    target: "instafeed-gallery-feed",
  });
galleryFeed.run();
def define_env(env):
    @env.filter
    def twitter(url):
        return f'<blockquote class="twitter-tweet"><a href="{url}"></a></blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'

    @env.filter
    def vimeo(videoid):
        return f'<iframe src="https://player.vimeo.com/video/{videoid}" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>'

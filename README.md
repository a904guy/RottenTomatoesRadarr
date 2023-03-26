# Rotten Tomatoes Radarr Feed Generator

I currently live at https://faas-nyc1-2ef2e6cc.doserverless.co/api/v1/web/fn-18d63adc-f8ea-472d-a5b1-4c103d2c8a72/rtr/convert

What a mouth full... Thanks to Digital Ocean for not making serverless functions easily mapable with just DNS. Get this, they recommend using a load balancer, which kind of defeats the purpose of serverless architecture, but I digress.

Just copy your url of your want to see list from Rotten Tomatoes and append it to the URL above.

So if your url is:

https://www.rottentomatoes.com/user/id/8b34fedb-2a09-49fe-802a-60b2d495975a/wts

Your feed URL is:

https://faas-nyc1-2ef2e6cc.doserverless.co/api/v1/web/fn-18d63adc-f8ea-472d-a5b1-4c103d2c8a72/rtr/convert/user/id/8b34fedb-2a09-49fe-802a-60b2d495975a/wts


When inserting into Lists use "Custom List" type.

FROM nginx

COPY ./etc/ssl/certs/nginx-selfsigned.crt /etc/ssl/certs/nginx-selfsigned.crt
COPY ./etc/ssl/private/nginx-selfsigned.key /etc/ssl/private/nginx-selfsigned.key
COPY ./etc/nginx/dhparam.pem /etc/nginx/dhparam.pem
COPY ./etc/nginx/ssl-params.conf /etc/nginx/snippets/ssl-params.conf
COPY ./etc/nginx/self-signed.conf /etc/nginx/snippets/self-signed.conf

COPY ./etc/nginx/nginx.conf /etc/nginx/nginx.conf

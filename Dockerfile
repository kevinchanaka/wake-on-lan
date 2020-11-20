FROM python:3.9-slim
COPY wol.py /
ENV MAC aa:bb:cc:dd:ee:ff
ENV BROADCAST 192.168.0.255
CMD python wol.py
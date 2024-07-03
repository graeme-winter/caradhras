# Caradhras

A replacement for the "ridgeway" component of the Pilatus system, using a zero-MQ stream in place of the filesystem copy operation which was previously used. This will need two components: a source running on the PPU and a sink running on a good GPFS connected host machine, with a decent ethernet (i.e. TCP/IP) connection between them.

## Source

On the HOST machine run:

```
python3 source.py
```

This will push the data as multipart messages on a stream for files found on the working directory.

## Sink

On the filesystem-mounted machine run

```
python3 sink.py source-host-name
```

Which will fetch the files and write them locally with the full filename they were delivered with.

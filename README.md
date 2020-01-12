
  <a href="https://github.com/s0md3v/velocity">
  <p align=center><img src=https://i.ibb.co/M7Ms4yS/velocity.png alt=velocity width=140px height=140px></p>
  </a>
<p align="center">
  <a href="https://github.com/s0md3v/velocity/releases">
    <img src="https://img.shields.io/github/release/s0md3v/velocity.svg">
  </a>
  <a href="https://github.com/s0md3v/velocity/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/s0md3v/velocity.svg">
  </a>
</p>

Velocity is an elegant DNS caching library for Python. It intercepts all the DNS/Protocol resolution calls and caches them.
That's it, everything that makes network connections gets a performance boost.

Liked the project? [Buy me a coffee.](https://github.com/s0md3v/velocity/new/master?readme=1#liked-the-project)

## Documentation
- [Installation](https://github.com/s0md3v/velocity/new/master?readme=1#installation)
- [Getting started](https://github.com/s0md3v/velocity/new/master?readme=1#getting-started)
- [Managing local cache](https://github.com/s0md3v/velocity/new/master?readme=1#managing-local-cache)
- [Manually caching hostnames](https://github.com/s0md3v/velocity/new/master?readme=1#manually-caching-hostnames)
- [Accessing cache databases](https://github.com/s0md3v/velocity/new/master?readme=1#accessing-cache-databases)

#### Installation
The recommended way to install **velocity** is by using pip as follows:
```
pip install velocity
```

#### Getting started
Velocity just needs to be imported to be activated.
For example, the following program will start using cached DNS responses after the first request.

```python
import requests
import velocity

for i in range(10):
     requests.get('https://s0md3v.github.io')

```

> **Important:** If you are using threads, consider caching the hostnames manually to prevent the database getting
affected from race conditions.

#### Managing local cache
The cache can be stored locally. None of the following methods return anything or take arguments, just call them at will.

```python
import velocity

velocity.flush_db()  # deletes the local cache
velocity.save_db()   # saves the in-memory cache locally
velocity.load_db()   # loads the local cache into memory
```

#### Manually caching hostnames
A hostname can be cached manually as follows:
```python
import velocity

velocity.cache(hostname)
```

> Note: IPv6 address are mapped to IPv4 addresses by default, which shouldn't be a problem. To avoid this behaviour and use IPv6 address instead, add an reachable port number as `velocity.cache(hostname, port)`

#### Accessing database
In-memory cache databases can be accessed with their respective variable names.
- `velocity.dns_cache` : Contains {hostname:ip} pairs
- `velocity.addr_cache` : Contains {hostname:getaddrinfo_object} pairs

### Contributions & License
Feel free to report any bugs you encounter, request features, give suggestions and fix bugs.

Pull requests that do not imrpove *velocity* as a program will not be accepted. Such as typo fixes, adding `.gitignore` file,
pep8 styled code structure etc.

Licensed under the GPLv3, see [LICENSE](https://github.com/s0md3v/velocity/blob/master/LICENSE) for more information.

### Liked the project?
You can support the developer by leaving a tip.

- [Paypal](https://paypal.me/s0md3v)
- [Patreon](https://www.patreon.com/s0md3v)

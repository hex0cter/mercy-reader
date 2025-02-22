# mercy-reader
A python library to extract clean(er), readable text from web pages, inspired by [zyocum's reader](https://github.com/zyocum/reader).

## Prerequisite
Please install [mercury-parser](https://github.com/postlight/mercury-parser) beforehand.
```
# Install Mercury globally
yarn global add @postlight/mercury-parser
#   or
npm -g install @postlight/mercury-parser
```

## Install

Install it as a Python dependency:

```
pip install mercy-reader
```

## Usage

```python
from mercy_reader import reader
from os import path

test_data_path = path.join(path.dirname(__file__), "data.json")
obj = reader.main(
        reader.load(test_data_path),
        80,
    )
print(reader.Format.formatter['md'](obj))

```

### Supported formats:
* md
* json
* txt

## Examples

### Mercury Web Parser JSON

The library takes Mercury Web Parser's JSON results as its input. Below is an example:
```json
{
  "title": "Mercury Goes Open Source! — Postlight — Digital product studio",
  "author": "Adam Pash",
  "date_published": "2019-02-06T14:36:45.000Z",
  "dek": null,
  "lead_image_url": "https://postlight.com/wp-content/uploads/2019/02/mercury-open-source-social-card-e1550670446269.png",
  "content": {
    "html": "<div class=\"body__content\"> <p>It&#x2019;s my pleasure to announce that today, Postlight is open-sourcing the <a href=\"https://mercury.postlight.com/web-parser/\">Mercury Web Parser</a>.</p>\n<p>Written in JavaScript and running on both Node and in the browser, Mercury Parser is the engine that powers the Mercury Parser API, <a href=\"https://mercury.postlight.com/amp-converter/\">Mercury AMP Converter</a>, <a href=\"https://mercury.postlight.com/reader/\">Mercury Reader</a>, and <a href=\"https://postlight.com/trackchanges/the-secret-engines-of-the-internet\">even more third-party software and services.</a></p>\n<p>Mercury Parser allows for better reading experiences, easier content migration, and endless opportunities for remixing the web, by making semantic sense out of any article. Mercury Parser sees web pages the same way you do: It sees titles, content, authors, and lead images, and makes all of that extracted data easily available to your software, which, unfortunately, sees only a sea of HTML markup, where page navigation, advertising, and the like are indistinguishable from content.</p>\n<p>Get <a href=\"https://github.com/postlight/mercury-parser\">Mercury Parser</a> for use in your projects on GitHub:</p>\n<blockquote class=\"embedly-card\"> <p>&#x1F4DC; Extracting content from the chaos of the web. Contribute to postlight/mercury-parser development by creating an account on GitHub.</p>\n</blockquote> <h3>Try Mercury Parser</h3>\n<p>Wanna see Mercury Parser in action in your own command line? First install it:</p>\n<pre>$ yarn global add @postlight/mercury-parser</pre>\n<p>Then parse an article and check out the results:</p>\n<pre>$ mercury-parser https://postlight.com/trackchanges/mercury-goes-open-source</pre>\n<p>Now, as an open-source project &#x2014; and with your help &#x2014; we hope to make the Mercury Parser even better. Say, for example, Mercury&#x2019;s done a less-than-perfect job parsing an article from your favorite web site. You can <a href=\"https://github.com/postlight/mercury-parser/blob/master/src/extractors/custom/README.md\">write and submit a custom site parser</a> guaranteed to get it right quickly, every time. We&#x2019;re excited about <a href=\"https://github.com/postlight/mercury-parser/blob/master/CONTRIBUTING.md\">all sorts of ways</a> the Mercury community will contribute to this project.</p>\n<h3>What about the API?</h3>\n<p>Over time, we will deprecate the Mercury Parser API. We&#x2019;ll do it slowly, with lots of warning and advance email notifications, and <a href=\"https://github.com/postlight/mercury-parser-api\">drop-in replacement code</a>. We&#x2019;ve committed to creating an easy path for people who want to use Mercury in any way they see fit, using open source, well-documented code that can be easily rolled into any other service or API. We want to put our energy there, making a more tractable web together&#x2014;not behind a private, hosted API.</p>\n<p>Indeed, one of the main drivers for this choice was API users asking us to open source Mercury&#x2014;and asking how they could help improve it.</p>\n<p>Today we&#x2019;ve done exactly that. You can use Mercury Parser directly in any JavaScript project, whether on Node or in your browser, starting today, with no API required. If you&#x2019;d like to chat about the Mercury Parser or need some help getting started, join the community in the <a href=\"https://gitter.im/postlight/mercury\">Mercury Gitter channel</a>.</p>\n<p><em><a href=\"https://postlight.com/trackchanges/authors/adam-pash\">Adam Pash</a> is a Director of Engineering at Postlight. Want help making sense of big messy data? Get in touch: <a href=\"https://postlight.com/cdn-cgi/l/email-protection#1a727f7676755a6a75696e76737d726e34797577\"><span class=\"__cf_email__\">[email&#xA0;protected]</span></a>.</em></p> </div>",
    "markdown": "It's my pleasure to announce that today, Postlight is open-sourcing the [Mercury Web Parser](https://mercury.postlight.com/web-parser/).\n\nWritten in JavaScript and running on both Node and in the browser, Mercury Parser is the engine that powers the Mercury Parser API, [Mercury AMP Converter](https://mercury.postlight.com/amp-converter/), [Mercury Reader](https://mercury.postlight.com/reader/), and [even more third-party software and services.](https://postlight.com/trackchanges/the-secret-engines-of-the-internet)\n\nMercury Parser allows for better reading experiences, easier content migration, and endless opportunities for remixing the web, by making semantic sense out of any article. Mercury Parser sees web pages the same way you do: It sees titles, content, authors, and lead images, and makes all of that extracted data easily available to your software, which, unfortunately, sees only a sea of HTML markup, where page navigation, advertising, and the like are indistinguishable from content.\n\nGet [Mercury Parser](https://github.com/postlight/mercury-parser) for use in your projects on GitHub:\n\n> 📜 Extracting content from the chaos of the web. Contribute to postlight/mercury-parser development by creating an account on GitHub.\n\n### Try Mercury Parser\n\nWanna see Mercury Parser in action in your own command line? First install it:\n    \n    \n    $ yarn global add @postlight/mercury-parser\n\nThen parse an article and check out the results:\n    \n    \n    $ mercury-parser https://postlight.com/trackchanges/mercury-goes-open-source\n\nNow, as an open-source project -- and with your help -- we hope to make the Mercury Parser even better. Say, for example, Mercury's done a less-than-perfect job parsing an article from your favorite web site. You can [write and submit a custom site parser](https://github.com/postlight/mercury-parser/blob/master/src/extractors/custom/README.md) guaranteed to get it right quickly, every time. We're excited about [all sorts of ways](https://github.com/postlight/mercury-parser/blob/master/CONTRIBUTING.md) the Mercury community will contribute to this project.\n\n### What about the API?\n\nOver time, we will deprecate the Mercury Parser API. We'll do it slowly, with lots of warning and advance email notifications, and [drop-in replacement code](https://github.com/postlight/mercury-parser-api). We've committed to creating an easy path for people who want to use Mercury in any way they see fit, using open source, well-documented code that can be easily rolled into any other service or API. We want to put our energy there, making a more tractable web together--not behind a private, hosted API.\n\nIndeed, one of the main drivers for this choice was API users asking us to open source Mercury--and asking how they could help improve it.\n\nToday we've done exactly that. You can use Mercury Parser directly in any JavaScript project, whether on Node or in your browser, starting today, with no API required. If you'd like to chat about the Mercury Parser or need some help getting started, join the community in the [Mercury Gitter channel](https://gitter.im/postlight/mercury).\n\n_[Adam Pash](https://postlight.com/trackchanges/authors/adam-pash) is a Director of Engineering at Postlight. Want help making sense of big messy data? Get in touch: [ [email protected]](https://postlight.com/cdn-cgi/l/email-protection#1a727f7676755a6a75696e76737d726e34797577)._\n",
    "text": "It's my pleasure to announce that today, Postlight is open-sourcing the Mercury Web Parser.\n\nWritten in JavaScript and running on both Node and in the browser, Mercury Parser is the engine that powers the Mercury Parser API, Mercury AMP Converter, Mercury Reader, and even more third-party software and services.\n\nMercury Parser allows for better reading experiences, easier content migration, and endless opportunities for remixing the web, by making semantic sense out of any article. Mercury Parser sees web pages the same way you do: It sees titles, content, authors, and lead images, and makes all of that extracted data easily available to your software, which, unfortunately, sees only a sea of HTML markup, where page navigation, advertising, and the like are indistinguishable from content.\n\nGet Mercury Parser for use in your projects on GitHub:\n\n> 📜 Extracting content from the chaos of the web. Contribute to postlight/mercury-parser development by creating an account on GitHub.\n\n### Try Mercury Parser\n\nWanna see Mercury Parser in action in your own command line? First install it:\n    \n    \n    $ yarn global add @postlight/mercury-parser\n\nThen parse an article and check out the results:\n    \n    \n    $ mercury-parser https://postlight.com/trackchanges/mercury-goes-open-source\n\nNow, as an open-source project -- and with your help -- we hope to make the Mercury Parser even better. Say, for example, Mercury's done a less-than-perfect job parsing an article from your favorite web site. You can write and submit a custom site parser guaranteed to get it right quickly, every time. We're excited about all sorts of ways the Mercury community will contribute to this project.\n\n### What about the API?\n\nOver time, we will deprecate the Mercury Parser API. We'll do it slowly, with lots of warning and advance email notifications, and drop-in replacement code. We've committed to creating an easy path for people who want to use Mercury in any way they see fit, using open source, well-documented code that can be easily rolled into any other service or API. We want to put our energy there, making a more tractable web together--not behind a private, hosted API.\n\nIndeed, one of the main drivers for this choice was API users asking us to open source Mercury--and asking how they could help improve it.\n\nToday we've done exactly that. You can use Mercury Parser directly in any JavaScript project, whether on Node or in your browser, starting today, with no API required. If you'd like to chat about the Mercury Parser or need some help getting started, join the community in the Mercury Gitter channel.\n\nAdam Pash is a Director of Engineering at Postlight. Want help making sense of big messy data? Get in touch: [email protected].\n"
  },
  "next_page_url": null,
  "url": "https://postlight.com/trackchanges/mercury-goes-open-source",
  "domain": "postlight.com",
  "excerpt": "It’s my pleasure to announce that today, Postlight is open-sourcing the Mercury Web Parser. Written in JavaScript and running on both Node and in the ...",
  "word_count": 436,
  "direction": "ltr",
  "total_pages": 1,
  "rendered_pages": 1
}
```

### HTML output
```html
<div class="body__content"> <p>It&#x2019;s my pleasure to announce that today, Postlight is open-sourcing the <a href="https://mercury.postlight.com/web-parser/">Mercury Web Parser</a>.</p>
<p>Written in JavaScript and running on both Node and in the browser, Mercury Parser is the engine that powers the Mercury Parser API, <a href="https://mercury.postlight.com/amp-converter/">Mercury AMP Converter</a>, <a href="https://mercury.postlight.com/reader/">Mercury Reader</a>, and <a href="https://postlight.com/trackchanges/the-secret-engines-of-the-internet">even more third-party software and services.</a></p>
<p>Mercury Parser allows for better reading experiences, easier content migration, and endless opportunities for remixing the web, by making semantic sense out of any article. Mercury Parser sees web pages the same way you do: It sees titles, content, authors, and lead images, and makes all of that extracted data easily available to your software, which, unfortunately, sees only a sea of HTML markup, where page navigation, advertising, and the like are indistinguishable from content.</p>
<p>Get <a href="https://github.com/postlight/mercury-parser">Mercury Parser</a> for use in your projects on GitHub:</p>
<blockquote class="embedly-card"> <p>&#x1F4DC; Extracting content from the chaos of the web. Contribute to postlight/mercury-parser development by creating an account on GitHub.</p>
</blockquote> <h3>Try Mercury Parser</h3>
<p>Wanna see Mercury Parser in action in your own command line? First install it:</p>
<pre>$ yarn global add @postlight/mercury-parser</pre>
<p>Then parse an article and check out the results:</p>
<pre>$ mercury-parser https://postlight.com/trackchanges/mercury-goes-open-source</pre>
<p>Now, as an open-source project &#x2014; and with your help &#x2014; we hope to make the Mercury Parser even better. Say, for example, Mercury&#x2019;s done a less-than-perfect job parsing an article from your favorite web site. You can <a href="https://github.com/postlight/mercury-parser/blob/master/src/extractors/custom/README.md">write and submit a custom site parser</a> guaranteed to get it right quickly, every time. We&#x2019;re excited about <a href="https://github.com/postlight/mercury-parser/blob/master/CONTRIBUTING.md">all sorts of ways</a> the Mercury community will contribute to this project.</p>
<h3>What about the API?</h3>
<p>Over time, we will deprecate the Mercury Parser API. We&#x2019;ll do it slowly, with lots of warning and advance email notifications, and <a href="https://github.com/postlight/mercury-parser-api">drop-in replacement code</a>. We&#x2019;ve committed to creating an easy path for people who want to use Mercury in any way they see fit, using open source, well-documented code that can be easily rolled into any other service or API. We want to put our energy there, making a more tractable web together&#x2014;not behind a private, hosted API.</p>
<p>Indeed, one of the main drivers for this choice was API users asking us to open source Mercury&#x2014;and asking how they could help improve it.</p>
<p>Today we&#x2019;ve done exactly that. You can use Mercury Parser directly in any JavaScript project, whether on Node or in your browser, starting today, with no API required. If you&#x2019;d like to chat about the Mercury Parser or need some help getting started, join the community in the <a href="https://gitter.im/postlight/mercury">Mercury Gitter channel</a>.</p>
<p><em><a href="https://postlight.com/trackchanges/authors/adam-pash">Adam Pash</a> is a Director of Engineering at Postlight. Want help making sense of big messy data? Get in touch: <a href="https://postlight.com/cdn-cgi/l/email-protection#4d25282121220d3d223e3921242a2539632e2220"><span class="__cf_email__">[email&#xA0;protected]</span></a>.</em></p> </div>
```

### Markdown output
```markdown
date: 2019-02-06 14:36:45  
author(s): Adam Pash  

# [Mercury Goes Open Source! — Postlight — Digital product studio](https://postlight.com/trackchanges/mercury-goes-open-source)

It's my pleasure to announce that today, Postlight is open-sourcing the [Mercury Web Parser](https://mercury.postlight.com/web-parser/).

Written in JavaScript and running on both Node and in the browser, Mercury Parser is the engine that powers the Mercury Parser API, [Mercury AMP Converter](https://mercury.postlight.com/amp-converter/), [Mercury Reader](https://mercury.postlight.com/reader/), and [even more third-party software and services.](https://postlight.com/trackchanges/the-secret-engines-of-the-internet)

Mercury Parser allows for better reading experiences, easier content migration, and endless opportunities for remixing the web, by making semantic sense out of any article. Mercury Parser sees web pages the same way you do: It sees titles, content, authors, and lead images, and makes all of that extracted data easily available to your software, which, unfortunately, sees only a sea of HTML markup, where page navigation, advertising, and the like are indistinguishable from content.

Get [Mercury Parser](https://github.com/postlight/mercury-parser) for use in your projects on GitHub:

> 📜 Extracting content from the chaos of the web. Contribute to postlight/mercury-parser development by creating an account on GitHub.

### Try Mercury Parser

Wanna see Mercury Parser in action in your own command line? First install it:
    
    
    $ yarn global add @postlight/mercury-parser

Then parse an article and check out the results:
    
    
    $ mercury-parser https://postlight.com/trackchanges/mercury-goes-open-source

Now, as an open-source project -- and with your help -- we hope to make the Mercury Parser even better. Say, for example, Mercury's done a less-than-perfect job parsing an article from your favorite web site. You can [write and submit a custom site parser](https://github.com/postlight/mercury-parser/blob/master/src/extractors/custom/README.md) guaranteed to get it right quickly, every time. We're excited about [all sorts of ways](https://github.com/postlight/mercury-parser/blob/master/CONTRIBUTING.md) the Mercury community will contribute to this project.

### What about the API?

Over time, we will deprecate the Mercury Parser API. We'll do it slowly, with lots of warning and advance email notifications, and [drop-in replacement code](https://github.com/postlight/mercury-parser-api). We've committed to creating an easy path for people who want to use Mercury in any way they see fit, using open source, well-documented code that can be easily rolled into any other service or API. We want to put our energy there, making a more tractable web together--not behind a private, hosted API.

Indeed, one of the main drivers for this choice was API users asking us to open source Mercury--and asking how they could help improve it.

Today we've done exactly that. You can use Mercury Parser directly in any JavaScript project, whether on Node or in your browser, starting today, with no API required. If you'd like to chat about the Mercury Parser or need some help getting started, join the community in the [Mercury Gitter channel](https://gitter.im/postlight/mercury).

_[Adam Pash](https://postlight.com/trackchanges/authors/adam-pash) is a Director of Engineering at Postlight. Want help making sense of big messy data? Get in touch: [ [email protected]](https://postlight.com/cdn-cgi/l/email-protection#86eee3eaeae9c6f6e9f5f2eaefe1eef2a8e5e9eb)._

```
### Plain-text output
```text
url: https://postlight.com/trackchanges/mercury-goes-open-source
date: 2019-02-06 14:36:45
author(s): Adam Pash

Mercury Goes Open Source! — Postlight — Digital product studio

It's my pleasure to announce that today, Postlight is open-sourcing the Mercury Web Parser.

Written in JavaScript and running on both Node and in the browser, Mercury Parser is the engine that powers the Mercury Parser API, Mercury AMP Converter, Mercury Reader, and even more third-party software and services.

Mercury Parser allows for better reading experiences, easier content migration, and endless opportunities for remixing the web, by making semantic sense out of any article. Mercury Parser sees web pages the same way you do: It sees titles, content, authors, and lead images, and makes all of that extracted data easily available to your software, which, unfortunately, sees only a sea of HTML markup, where page navigation, advertising, and the like are indistinguishable from content.

Get Mercury Parser for use in your projects on GitHub:

> 📜 Extracting content from the chaos of the web. Contribute to postlight/mercury-parser development by creating an account on GitHub.

### Try Mercury Parser

Wanna see Mercury Parser in action in your own command line? First install it:
    
    
    $ yarn global add @postlight/mercury-parser

Then parse an article and check out the results:
    
    
    $ mercury-parser https://postlight.com/trackchanges/mercury-goes-open-source

Now, as an open-source project -- and with your help -- we hope to make the Mercury Parser even better. Say, for example, Mercury's done a less-than-perfect job parsing an article from your favorite web site. You can write and submit a custom site parser guaranteed to get it right quickly, every time. We're excited about all sorts of ways the Mercury community will contribute to this project.

### What about the API?

Over time, we will deprecate the Mercury Parser API. We'll do it slowly, with lots of warning and advance email notifications, and drop-in replacement code. We've committed to creating an easy path for people who want to use Mercury in any way they see fit, using open source, well-documented code that can be easily rolled into any other service or API. We want to put our energy there, making a more tractable web together--not behind a private, hosted API.

Indeed, one of the main drivers for this choice was API users asking us to open source Mercury--and asking how they could help improve it.

Today we've done exactly that. You can use Mercury Parser directly in any JavaScript project, whether on Node or in your browser, starting today, with no API required. If you'd like to chat about the Mercury Parser or need some help getting started, join the community in the Mercury Gitter channel.

Adam Pash is a Director of Engineering at Postlight. Want help making sense of big messy data? Get in touch: [email protected].

```

### Run the test
```bash
python setup.py pytest --addopts -s
```

## References
* [mercury-parser](https://github.com/postlight/mercury-parser)
* [zyocum's reader](https://github.com/zyocum/reader)

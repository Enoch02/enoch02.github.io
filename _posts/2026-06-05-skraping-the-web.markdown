---
layout: post
title:  Skraping The Web
date:   2026-06-5 20:47:22 +0100
categories: software
---
When I think of the term Web Scraping, Python comes to mind, and then Beautiful Soup does too. A long, long time ago, I needed to scrape some web content for an Android app, so I went on the interwebs to do some "research". The first library I discovered was JSoup; it worked alright but was not Kotlin-y enough for my tastes, so I continued my journey until I discovered skrape{it}.

skrape{it} is based on JSoup and uses a DSL which is really nice to use. The following is an example:
```kotlin
htmlDocument {
    div {
        withId = "imgs"

        findFirst {
            chapterName = attribute("data-alt")

            img {
                findAll {
                    forEach {
                        val imgUrl = it.attribute("data-src")
                        pageURLs.add(imgUrl)
                    }
                }
            }
        }
    }
}
```

## Getting Started

To start using **skrape{it}** in a Kotlin project, add the library to your build configuration and write a small scraping script.

### 1. Add the dependency

If you are using Gradle (Kotlin DSL), include the following in your `build.gradle.kts`:

```kotlin
repositories {
    mavenCentral()
}

dependencies {
    implementation("it.skrape:skrapeit:1.2.2") // check for the latest version
}
```

For Maven, add:

```xml
<dependency>
    <groupId>it.skrape</groupId>
    <artifactId>skrapeit</artifactId>
    <version>1.2.2</version>
</dependency>
```

### 2. Write a scraper

Create a Kotlin file, e.g., `ScrapeExample.kt`, and use the DSL:

```kotlin
import it.skrape.core.htmlDocument
import it.skrape.fetcher.HttpFetcher
import it.skrape.fetcher.response
import it.skrape.fetcher.skrape
import it.skrape.selects.html5.h1
import it.skrape.selects.html5.p

fun main() {
    skrape(HttpFetcher) {
        request {
            url = "https://example.com"
        }

        response {
            htmlDocument {
                h1 {
                    findFirst { println("The first H1 tag contains the text: $text") }
                }

                println("The site contains the following paragraphs: ")
                p {
                    findAll {
                        forEach {
                            println(it)
                        }
                    }
                }
            }
        }
    }
}
```


### 3. Run the program

Compile and run with Gradle:

```bash
./gradlew run
```
Or, just click the run button in your IDE (ctrl+r or shift+f10). That’s it! Your first skrape{it} scraper is ready!

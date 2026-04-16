+++
title = "Local LLaMAs: Part 1"
date = "2026-04-14"
author = "Doug Flick"
cover = "img/LocalLLaMA.jpeg"
description = "Local LLAMAs: Part 1 - Where to get started"
keywords = ['AI', 'Coding', 'VsCode', 'Basic AI']
+++


Large Language Models are rapidly changing how we architect, write, and review code.However, relying solely on hosted APIs from Anthropic or OpenAI can get expensive, especially when you're just experimenting or learning a new library.

I also wanted to get a better grasp of how this technology works under the hood without sending every prompt to a third-party server. To that end, I’m starting a series of posts to document my journey of setting up local tools and discussing what works, what breaks, and what's worth the effort.

If you're looking for deep technical dives into the architecture, I highly recommend [this post on MicroGPT](https://growingswe.com/blog/microgpt) as a foundational resource.

Finding a starting point in the local LLM space is overwhelming. I spent a some ime lurking in [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/), but can feel like drinking from a firehose.

Most of the community consensus points toward [Ollama](https://ollama.com/) as the easiest first step. I decided to test it out to see if the "ease of use" claims held up. And it was - I very quickly had a Llama3 Model up and running and responding but then I immediatly had new questions.

1. Why are internet searches rate limited?
2. How can I use this model for Assisted Programming?

# LangChain + Local LLMs + dstack

In this talk, you'll learn two things:

1. How and why to use `langchain` with local LLMs
2. How to use `dstack` to streamline ML development in the cloud

As we build a chat app (using the [Falcon-7B-Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct) LLM).

### Agenda

0. Poll.
1. [What is LangChain?](langchain_intro.ipynb)
2. [Local LLMs with LangChain](local_llms_intro.ipynb)
3. [Dev environments with dstack](dstack_into.ipynb)
4. [Using Falcon with LangChain](falcon_with_langchain.ipynb)
5. [Building a chat app](skeleton.py)
6. [Automating tasks with dstack](dstack_into.ipynb)
7. Q&A

To work with this repo, make sure to install the latest version of `dstack`: 

```shell
pip install "dstack[aws,gcp,azure] -U"`
```

> If you have any questions about `dstack`, please ask them in [Slack](https://join.slack.com/t/dstackai/shared_invite/zt-xdnsytie-D4qU9BvJP8vkbkHXdi6clQ).

### References

- [Pinecone's LangChain Handbook](https://www.pinecone.io/learn/langchain/)
- [Hugging Face Local Pipelines](https://python.langchain.com/en/latest/modules/models/llms/integrations/huggingface_pipelines.html)
- [Falcon-7B-Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct)
- [Dolly 2.0's instruct pipeline](https://huggingface.co/databricks/dolly-v2-12b/raw/main/instruct_pipeline.py)
- [dstack Docs](https://dstack.ai/docs/)
- [Source code](https://github.com/dstackai/langchain-meetup)
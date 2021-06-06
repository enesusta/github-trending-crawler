
**github-trending-crawler**

---

`github-trending-crawler` is a basic rest API that crawls github.com/trending.

![](https://raw.githubusercontent.com/enesusta/assets-host-for-github-pages/assets/github-trending-crawler/github-trending-crawler.gif)


- [Install](#install)
  - [Docker](#docker)
- [Sample Request](#sample-request)
- [Sample Response](#sample-response)

## Install

github-trending-crawler runs on `5000 HTTP` port.

### Docker

You can mapping the ports whatever you want. The most important thing about github-trending-crawler port mapping is that github-trending-crawler runs on `5000 HTTP` port. You must consider this during configure your mapping.

- With CLI

```bash
docker run -d -p 8080:5000 enesusta/github-trending-crawler:20210606
```

- With docker-compose

Let's look at this sample.

`docker-compose.yml`

```yml
version: '3'

services:
  github-trending-crawler:
    container_name: github-trending-crawler
    image: enesusta/github-trending-crawler:20210606
    ports:
    - 8080:5000
```

Then:

```bash
docker-compose up -d
```

github-trending-crawler needs a query parameters which named **lang**. You have to give this parameter on your http calls to github-trending-crawler.

You can get trending information of any language that listed below that picture has.

![](https://raw.githubusercontent.com/enesusta/assets-host-for-github-pages/assets/github-trending-crawler/github-trending.png)


## Sample Request

```http
http://localhost:8080?lang=go
```

## Sample Response

```json
[
   {
      "description":"Render markdown on the CLI, with pizzazz! 💅🏻",
      "repository":"https://github.com/charmbracelet/glow",
      "stars":"94 stars today"
   },
   {
      "description":"Temporal service and CLI",
      "repository":"https://github.com/temporalio/temporal",
      "stars":"72 stars today"
   },
   {
      "description":"gRPC to JSON proxy generator following the gRPC HTTP spec",
      "repository":"https://github.com/grpc-ecosystem/grpc-gateway",
      "stars":"53 stars today"
   },
   {
      "description":"Create beautiful system diagrams with Go",
      "repository":"https://github.com/blushft/go-diagrams",
      "stars":"46 stars today"
   },
   {
      "description":"⚡️ Fiber is an Express inspired web framework written in Go with ☕️",
      "repository":"https://github.com/gofiber/fiber",
      "stars":"44 stars today"
   },
   {
      "description":"Personal Photo Management powered by Go and Google TensorFlow",
      "repository":"https://github.com/photoprism/photoprism",
      "stars":"28 stars today"
   },
   {
      "description":"Terraform enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.",
      "repository":"https://github.com/hashicorp/terraform",
      "stars":"27 stars today"
   },
   {
      "description":"Cadence is a distributed, scalable, durable, and highly available orchestration engine to execute asynchronous long-running business logic in a scalable and resilient way.",
      "repository":"https://github.com/uber/cadence",
      "stars":"20 stars today"
   },
   {
      "description":"A Commander for modern Go CLI interactions",
      "repository":"https://github.com/spf13/cobra",
      "stars":"16 stars today"
   },
   {
      "description":"CockroachDB - the open source, cloud-native distributed SQL database.",
      "repository":"https://github.com/cockroachdb/cockroach",
      "stars":"13 stars today"
   },
   {
      "description":"High Performance, Kubernetes Native Object Storage",
      "repository":"https://github.com/minio/minio",
      "stars":"13 stars today"
   },
   {
      "description":"Nomad is an easy-to-use, flexible, and performant workload orchestrator that can deploy a mix of microservice, batch, containerized, and non-containerized applications. Nomad is easy to operate and scale and has native Consul and Vault integrations.",
      "repository":"https://github.com/hashicorp/nomad",
      "stars":"10 stars today"
   },
   {
      "description":"Argo Workflows: Get stuff done with Kubernetes.",
      "repository":"https://github.com/argoproj/argo",
      "stars":"10 stars today"
   },
   {
      "description":"Application Kernel for Containers",
      "repository":"https://github.com/google/gvisor",
      "stars":"8 stars today"
   },
   {
      "description":"Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.",
      "repository":"https://github.com/hashicorp/packer",
      "stars":"8 stars today"
   },
   {
      "description":"A Vault swiss-army knife: a K8s operator, Go client with automatic token renewal, automatic configuration, multiple unseal options and more. A CLI tool to init, unseal and configure Vault (auth methods, secret engines). Direct secret injection into Pods.",
      "repository":"https://github.com/banzaicloud/bank-vaults",
      "stars":"7 stars today"
   },
   {
      "description":"Declarative continuous deployment for Kubernetes.",
      "repository":"https://github.com/argoproj/argo-cd",
      "stars":"7 stars today"
   },
   {
      "description":"GoMock is a mocking framework for the Go programming language.",
      "repository":"https://github.com/golang/mock",
      "stars":"7 stars today"
   },
   {
      "description":"CLI tool for spawning and running containers according to the OCI specification",
      "repository":"https://github.com/opencontainers/runc",
      "stars":"7 stars today"
   },
   {
      "description":"High-Performance server for NATS, the cloud native messaging system.",
      "repository":"https://github.com/nats-io/nats-server",
      "stars":"6 stars today"
   },
   {
      "description":"Elasticsearch client for Go.",
      "repository":"https://github.com/olivere/elastic",
      "stars":"6 stars today"
   },
   {
      "description":"🐠 Beats - Lightweight shippers for Elasticsearch & Logstash",
      "repository":"https://github.com/elastic/beats",
      "stars":"4 stars today"
   },
   {
      "description":"Terraform provider for Azure Resource Manager",
      "repository":"https://github.com/terraform-providers/terraform-provider-azurerm",
      "stars":"3 stars today"
   },
   {
      "description":"Highly available Prometheus setup with long term storage capabilities. A CNCF Incubating project.",
      "repository":"https://github.com/thanos-io/thanos",
      "stars":"3 stars today"
   },
   {
      "description":"An in-memory key:value store/cache (similar to Memcached) library for Go, suitable for single-machine applications.",
      "repository":"https://github.com/patrickmn/go-cache",
      "stars":"3 stars today"
   }
]
```























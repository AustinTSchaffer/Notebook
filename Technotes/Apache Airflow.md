# Apache Airflow

## Personal Notes
- I could have built the PyPI scraper program using Airflow instead of using RabbitMQ and Docker Swarm
- Seems to fill a similar nice that AWS Step Functions fills

## What Airflow
- platform for developing, scheduling, and monitoring batch-oriented workflows
- Mostly python, can run bash scripts too
- Uses a DAG for controlling when tasks run, as tasks can and often do have dependencies on other tasks
- Allows cron scheduling
- Has workflow/task/operator parameterization
- Can run multiple workflows simultaneously

## Why Not Airflow
- Airflow was built for finite batch workflows.
- Airflow was not built for infinitely running event-based workflows.
- Airflow is not a streaming solution.
	- Kafka can be used for ingestion and processing in real-time, event data is written to a storage location (or kept in the topic)
	- Airflow can periodically start a workflow for processing a batch of data from the bucket's storage location (or from the topic itself, probably, a topic is a storage location)

## Core Concepts
- workflows are represented as DAGs
- nodes in the DAG are tasks
- tasks are individual pieces of work
- data flows between tasks
- The DAG specifies task dependencies, and therefore allows the system to schedule tasks in topological order
- tasks typically perform one of the following functions
	- fetching data
	- running analysis
	- triggering other systems
	- persisting results
	- sending emails

### Required Components
- scheduler
	- handles triggering scheduled workflows
	- submits tasks to the executer to run
	- executor
		- configuration property of the scheduler
		- not a separate component
		- runs within the scheduler process
- webserver
	- presents a handy UI
	- shows info about configured tasks and workflows, runtime stats, etc
- a folder of DAG files, read by the scheduler
- metadata database
	- stores the state of workflows and tasks

### Optional Components
- worker
	- executes tasks given by the scheduler
	- basic installation: worker is part of the scheduler and not a separate component
	- can be run as a long-running Celery process via the CeleryExecutor
	- can be a Kubernetes pod via the KubernetesExecutor
- triggerer
	- executes deferred tasks in an asyncio loop
	- not necessary if you're not using deferred tasks
- dag processor
	- parses DAG files and serializes them into the metadata database
	- by default, the dag processor is part of the scheduler
	- can be run as a separate component for scalability/security concerns
	- if this component is present, the scheduler does not read DAG files directly
- plugins folder
	- similar to installed packages
	- can extend the functionality of any component

### Deploying
- Airflow is designed to be deployed in a distributed cluster configuration
- Components can be isolated for security/scalability reasons

#### Basic Deployment
![[airflow-basic-deployment.png]]

- single machine deployment (you'll probably have the database on a different machine)
- uses the LocalExecutor (scheduler and workers are within/under the same Python process)
- DAG files are ready fro the local filesystem by the scheduler
- webserver runs on the same machine as the scheduler
- there is no triggerer, task deferral is not possible

#### Distributed Deployment
![[airflow-distributed-deployment.png]]

- multiple role types for different levels of access
- DAG files are synchronized between all components that use them
- Helm charts + Kubernetes are one of the ways for deploying Airflow to a K8s cluster

### Workloads
- DAGs run a series of tasks
- three common task types
	- Operators - predefined tasks that you can string together to build out most of your DAG
	- Sensors - special subclass of operator which are about waiting for external events to happen
	- TaskFlow-decorated `@task`, custom Python function packaged as a Task

### Control Flow
- Task dependencies are defined in code
- Airflow works out the order that tasks are executed in.
- Some options for customizing task execution order
	- branching
	- latestonly
	- trigger rules
- Data can be passed between tasks
	- XComms ("Cross-communications") - tasks can push and pull small bits of metadata
	- Large data transfer can happen via bucket storage / DB connections
	- TaskFlow API automatically passes data between tasks via implicit XComms
- You can use SubDAGs to make reusable DAG components that you can embed into larger DAGs
- TaskGroups let you visually group tasks in the UI
- Features for pre-configuring access to central resources like DBs
	- Connections and Hooks
	- Pools for limiting concurrency

### Operators
- Operators are templates for predefined Tasks. Popular ones include
	- BashOperator
	- PythonOperator (use `@task` decorator on arbitrary python functions)
	- EmailOperator
- There are community provider packages which enable you to effectively import task definitions that someone else maintains.
	- https://airflow.apache.org/docs/apache-airflow-providers/index.html
	- [`HttpOperator`](https://airflow.apache.org/docs/apache-airflow-providers-http/stable/_api/airflow/providers/http/operators/http/index.html#airflow.providers.http.operators.http.HttpOperator "(in apache-airflow-providers-http v4.11.1)")
	- [`MySqlOperator`](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/_api/airflow/providers/mysql/operators/mysql/index.html#airflow.providers.mysql.operators.mysql.MySqlOperator "(in apache-airflow-providers-mysql v5.6.1)")
	- [`PostgresOperator`](https://airflow.apache.org/docs/apache-airflow-providers-postgres/stable/_api/airflow/providers/postgres/operators/postgres/index.html#airflow.providers.postgres.operators.postgres.PostgresOperator "(in apache-airflow-providers-postgres v5.11.1)")
	- [`MsSqlOperator`](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-mssql/stable/_api/airflow/providers/microsoft/mssql/operators/mssql/index.html#airflow.providers.microsoft.mssql.operators.mssql.MsSqlOperator "(in apache-airflow-providers-microsoft-mssql v3.7.1)")
	- [`OracleOperator`](https://airflow.apache.org/docs/apache-airflow-providers-oracle/stable/_api/airflow/providers/oracle/operators/oracle/index.html#airflow.providers.oracle.operators.oracle.OracleOperator "(in apache-airflow-providers-oracle v3.10.1)")
	- [`JdbcOperator`](https://airflow.apache.org/docs/apache-airflow-providers-jdbc/stable/_api/airflow/providers/jdbc/operators/jdbc/index.html#airflow.providers.jdbc.operators.jdbc.JdbcOperator "(in apache-airflow-providers-jdbc v4.3.1)")
    - [`DockerOperator`](https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operators/docker/index.html#airflow.providers.docker.operators.docker.DockerOperator "(in apache-airflow-providers-docker v3.12.0)")
    - [`HiveOperator`](https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/_api/airflow/providers/apache/hive/operators/hive/index.html#airflow.providers.apache.hive.operators.hive.HiveOperator "(in apache-airflow-providers-apache-hive v8.1.1)")
    - [`S3FileTransformOperator`](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/_api/airflow/providers/amazon/aws/operators/s3/index.html#airflow.providers.amazon.aws.operators.s3.S3FileTransformOperator "(in apache-airflow-providers-amazon v8.24.0)")
    - [`PrestoToMySqlOperator`](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/_api/airflow/providers/mysql/transfers/presto_to_mysql/index.html#airflow.providers.mysql.transfers.presto_to_mysql.PrestoToMySqlOperator "(in apache-airflow-providers-mysql v5.6.1)")
    - [`SlackAPIOperator`](https://airflow.apache.org/docs/apache-airflow-providers-slack/stable/_api/airflow/providers/slack/operators/slack/index.html#airflow.providers.slack.operators.slack.SlackAPIOperator "(in apache-airflow-providers-slack v8.7.1)")
    - etc, you get the point
- Operators support Jinja templating, so you can pass in templates to Operators



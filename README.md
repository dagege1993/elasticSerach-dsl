# elasticSerach-dsl



# 基本概念：

## 简介：
        python官方针对elasticsearch操作的库，类似于orm之数据库

## 1.节点和集群
节点Node 是一个运行着的elasticsearch实例，你可以理解为单个服务器。

集群 是一个或多个节点的集合，协同工作，共享数据并且故障转移和扩展

## 3.文档：
文档是可索引信息基本单元，主要实体叫文档，Json表示，文档理解为数据库中的行列数据，一个文档相当于数据库
文档有几个共同不可缺的属性，分别是_index,_type,_id,对特定或一类文档进行操作，必须指定这些属性


## 4. 索引
索引相似特征的文档集合

Relational DB|	Elasticsearch
 
        Databases	 |  Indices(索引）

               Tables	 |      Types（类型）

                Rows  |     Documents（文档，数据库每一条数据）

          Columns	  |    Fields
          
 ## 5.映射
 模式映射，用于定义索引结构
          
          
            
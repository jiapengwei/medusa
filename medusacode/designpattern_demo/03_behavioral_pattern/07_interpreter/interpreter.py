#!/usr/bin/env python
# coding:utf-8

"""
解释器模式(Interpreter Pattern)
    定义语言(使用规定格式和语法的代码)的文法，并且建立一个解释器来解释该语言中的句子。

包含五个角色
包含如下几个角色：
    [AbstractExpression][抽象表达式]
        声明一个抽象的解释操作，该接口为抽象语法树中所有的节点共享。
    [TerminalExpression][终结符表达式]
        实现与文法中的终结符相关的解释操作。
        实现抽象表达式中所要求的方法。
        文法中每一个终结符都有一个具体的终结表达式与之相对应。
    [NonterminalExpression][非终结符表达式]
        为文法中的非终结符相关的解释操作。
    [Context][环境类]
        包含解释器之外的一些全局信息。
    [Client][客户类]

解释器模式描述了如何构成一个简单的语言解释器，主要应用在使用面向对象语言开发的编译器中。
它描述了如何为简单的语言定义一个文法，如何在该语言中表示一个句子，以及如何解释这些句子。

优点
    可扩展性比较好，灵活。
    增加了新的解释表达式的方式。
    易于实现文法。

缺点
    执行效率比较低，可利用场景比较少。
    对于复杂的文法比较难维护。

适用情况
    需要将一个需要解释执行的语言中的句子表示为一个抽象语法树。
    一些重复出现的问题可以用一种简单的语言来进行表达。
    文法较为简单。
"""




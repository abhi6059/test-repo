# Databricks notebook source
def main():
    return "Hello World"

# COMMAND ----------

def test_func():
    print("This is function to test branch behavior")

# COMMAND ----------

def test_func_v2():
    print("Adding another function from v2 to test sync of branch behavior")

# COMMAND ----------

def test_func_v1():
    print(2+2)
    print("Adding function from v1 to test merging in v2")

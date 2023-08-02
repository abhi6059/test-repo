# Databricks notebook source
def main():
    return "Hello World"

# COMMAND ----------

def test_func():
    print("This is function to test branch behavior")

# COMMAND ----------

def test_func_v2():
    print(2+3)
    print(3-1)
    print(2*2)
    print("Adding another function from v2 to test sync of branch behavior")
    print(5+3)
    print(5-2)

# COMMAND ----------

def test_func_v1():
    print(2+2)
    print("Adding function from v1 to test merging in v2")

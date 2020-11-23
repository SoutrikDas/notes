# pd.set_option()

Description: Lets you change various settings , for example maximum columns shown 
Tags: function

# Change it so that printing a dataframe actually shows all columns

---

First use `df.shape` attribute to get the number of columns, suppose 65 in this case , then set the number of maximum columns displayed to that 

```python
pd.set_option("display.max_columns", 65)
```
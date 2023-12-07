# Friend or Foe?

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

~~~if-not:factor
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
~~~

~~~if:factor
Ex: Input = `{ "Ryan" "Kieran" "Jason" "Yous" }`, Output = `{ "Ryan" "Yous" }`
~~~

i.e.
```haskell
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
```

```factor
{ "Ryan" "Kieran" "Mark" } friend -> { "Ryan" "Mark" }
```


Note: keep the original order of the names in the output.


[friend-or-foe](https://www.codewars.com/kata/55b42574ff091733d900002f)
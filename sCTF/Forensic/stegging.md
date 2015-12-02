#Problems

They give us 2 picture, original.jpg and stegged.jpg. First, i open stegging.jpg in paint and do something i always do but i can't find anything. So i try to use diff command to find different thing between these picture.

```
[quang@at10e Desktop]$ diff original.jpg stegged.jpg 
Binary files original.jpg and stegged.jpg differ
```

As we see, these file have differ binary. Lets try something to show those different binary. I use cmp command with to option is b and l.
The b option will print differing bytes and the l option output  byte numbers and difering byte values. Mix it together and we will get the flag.

```
[quang@at10e Desktop]$ cmp -bl stegged.jpg original.jpg 
   99   0 ^@   146 f
  100   0 ^@   154 l
  101   0 ^@   141 a
  102   0 ^@   147 g
  103   0 ^@   173 {
  104   0 ^@   171 y
  105   0 ^@    60 0
  106   0 ^@   165 u
  107   0 ^@   137 _
  108   0 ^@   150 h
  109   0 ^@   141 a
  110   0 ^@   166 v
  111   0 ^@   145 e
  112   0 ^@   137 _
  113   0 ^@   147 g
  114   0 ^@   162 r
  115   0 ^@   141 a
  116   0 ^@   144 d
  117   0 ^@   165 u
  118   0 ^@    64 4
  119   0 ^@   164 t
  120   0 ^@   145 e
  121   0 ^@   144 d
  122   0 ^@   137 _
  123   0 ^@   146 f
  124   0 ^@   162 r
  125   0 ^@    60 0
  126   0 ^@   155 m
  127   0 ^@   137 _
  128   0 ^@   164 t
  129   0 ^@   150 h
  130   0 ^@    63 3
  131   0 ^@   137 _
  132   0 ^@   142 b
  133   0 ^@   141 a
  134   0 ^@   142 b
  135   0 ^@   171 y
  136   0 ^@    47 '
  137   0 ^@    65 5
  138   0 ^@    40  
  139   0 ^@   142 b
  140   0 ^@    60 0
  141   0 ^@    67 7
  142   0 ^@    67 7
  143   0 ^@    61 1
  144   0 ^@    63 3
  145   0 ^@    41 !
  146   0 ^@    41 !
  147   0 ^@   175 }

```

**Flag is : flag{y0u_have_gradu4ted_fr0m_th3_baby'5 b07713!!}**

I'm not the one who solve this challenger. My friend told me about cmp command.

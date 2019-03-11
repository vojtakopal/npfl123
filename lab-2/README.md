#
The most complex data can is expected from news article (`all-the-news` dataset) resulting in highest entropy. DSTC2 dataset ended up with lowest entropy which I now realised is because I have only considered the systems output and have not included the customer requests. I don't really see a reason to have different results between DSTC2 and bAbI.

## DSTC2 dataset
```
Entropy: 4.606484316766185
```

## bAbI dataset
```
Entropy: 5.734474596715691
```

## All the news dataset
```
Entropy: 6.633388208100886
```
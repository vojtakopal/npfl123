## Phonetic transcription

See `phonetic-text.txt`

## Conversations bot

Concierge service bot. 

Task oriented for a set of tasks:
 * creating and updating reservations
 * dealing with room service tasks

Basic chitchat functionality.

It's an interface between hotels and guest to provide the basic service.

### 1st
```
Hi, I'd like to book a room.
Great, where are you travelling to?
To London.
London is a great choice! And when do you plan to arrive?
Tomorrow.
Tomorrow it is. How long do you want to stay?
For 3 days.
So to confirm, you want to stay in London starting from March 3rd to March 5th. Is that correct?
Yes.
Are you staying with someone else?
No.
We have rooms available in the City starting at 200 pounds. Do you prefer economy or business rooms?
Business.
Perfect. Business starts at 350 pounds. Do you have any preferences regarding your room?
No.
Great. Can we offer you a breakfast with your reservation? For you the price is 10 pounds per a breakfast.
Yes, please.
Amazing! It will be 630 pounds for your stay. Would that be all?
Yes.
You will be now redirected to our secured payment gateway. Good bye.
```

### 2nd

```
Hi, how can I help you?
There is a issue with my room.
What kind of issue?
My room fridge is empty.
I understand your fridge is empty. Do you want me to make ir full?
Yes, please.
We are sending you a room service to fill your fridge rightaway.
```

### 3rd

```
Hi.
Hey.
Tell me a joke.
Knock, knock.
Who’s there?
Robin.
Robin who?
Robin you, now hand over the cash.
```

### 4th

```
Hi.
Hi. I need help with my reservation.
What is your booking number?
2345678
I see your staying with us tomorrow. What is the problem?
I need to cancel it.
I see. There is a cancellation fee of 100%. Do you want to proceed?
No.
```

### 5th

```
Hi.
Hello.
```

## Minimum change distance

`python3 test_suite.py`

`dist(hyp, gold)` returns a pair of list of operations and calculated minimum distance.

operation: (name of operation [,characters]), e.g. 
  - ('n'): nothing, 
  - ('d', 'A'): delete A
  - ('i', 'B'): insert B
  - ('s', 'C', 'D'): subsitute C for D 

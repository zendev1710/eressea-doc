---
# cSpell:locale en
alias: optimize-learning-chains
---
# Optimization of learning chains

## Preliminary considerations

The first thing you should do when optimizing learning chains is to be clear about which assignments of teachers to students you prefer.  
Only then can you either create a set of rules (so-called expert knowledge) or write an optimization algorithm that produces the best or at least the best possible state (assignments of teachers and students).

All other approaches I have seen so far belong more to the category of expert knowledge.  
The Techer plugin from Magellan or the FF tools (2) should be mentioned here.  
The units are sorted according to a criterion and then processed.  
The assignments are created successively.  
An evaluation or comparison of different options only takes place at the lowest level.

This approach is by no means bad as it delivers good results in a great time.
In addition, the rules are clear and understandable and no one will be surprised why an assignment was made.

But I would also like to point out another possibility here: each partial state can be evaluated with a cost or profit and an estimation function, similar to route finding.
This means that a usually unattainable optimum can be defined to which one tries to trim the assignments.
The most important thing is the cost or profit function and then the estimation function derived from it.

## Cost - Profit function

Learning has costs, I think that is clear to everyone.
In Eressea it is the silver for maintenance or for the expensive talents.
If you are taught, the costs remain absolutely the same, but the learning effect is greater.
So you can say the costs per week of learning are reduced by half -right, not completely, because the teacher also wants to be paid.

You can also approach it the other way around and maximize the learning gain and assume the costs are constant (which is usually true).
This case suits us because teaching no longer means infinite costs (since we don't learn anything).

So a simple profit function could return the following values ​​per person (Example 1):

    Teacher            = 0
    Learn without a teacher = 1
    Learns with teacher  = 2

I can confirm this much, this function does what you would expect -it ensures that as many students as possible get a teacher.
Unfortunately, it does not evaluate the talents of teachers or students and thus ensures that sooner or later all units are within a range of 2-3 talent levels.
It will also happen that a teacher teaches a 2 person unit.

So, as mentioned at the beginning, it is important to be clear about some boundaries.
Then these limits, which unfortunately often have the opposite effect, must be integrated into the cost function.

### Limit cases for the cost function

The first thing you should do is determine how many students a teacher should have at least, even if the talent difference is only 2 levels.
Furthermore, one should clarify up to which level recruits can be taught, i.e. whether T20s can also teach T0s.
More generally, one specifies up to which talent difference, depending on the teacher's talent, how many students must be taught at least so that this allocation is more favorable than letting teacher and student learn.
The best thing to do here is to create a small diagram with the desired line/curve and then develop a function that covers it as well as possible.

I developed the following function for myself:

    A = 1.2
    B = 15
    C = 0.34
    Teacher            = 0
    Learn without a teacher = (A^Level + B) * (3^C)
    Learns with teacher  = (A^Level + B) * (6^C)

The parameters A, B and C were created after long tests and partly by equating various formulas.
The formula can also easily be used for brainwax and academy use by substituting the 3 or 6 for the number of learning attempts*3 is replaced.
So learning with brainpower results in (1 + 1/3)*3 = 4.

As you can calculate, learning with a teacher due to factor C is not twice as profitable as without a teacher, but is only worth around 27% more.
And because the level is included in the formula as a power, you gain much more if you teach 8 high-level people instead of 10 newbies.

## Estimator function

As mentioned, this should predict the profit as well as possible.
It is important not to underestimate the optimum.
But where is our optimum? Apparently not all people can be taught without there being a teacher.
This means that we can assume that each unit is taught in its entirety, but at the same time we have to deduct the minimum that a teacher could have achieved as profit.
A very good approximation for this results from:

Estimated Profit = Learn_with_Teacher(Level) -0.1 *Learn_with_Teacher(Level+2) + 0.01 *Learn_with_Teacher(Level+4)

This means we are definitely slightly above the possible optimum.

## A* Search

The A*-Search is probably familiar to some people from wayfinding.
In short, there are one or more target states, many intermediate states and of course a starting state somewhere.
These states are connected by edges.
If you walk along an edge you incur costs (or generate profit -depending on how you look at it).
A path is sought in the state graph that causes minimum costs or maximum profit.

The A*Search optimizes the search in the graph by not searching all possible paths, but rather specifically pursuing paths that have low estimated costs /high estimated profits.

How good the A*-Search works, so it depends heavily on the accuracy of the estimator.
Accuracy means how close the estimated value is to the actual optimal value.

### Learning states

It is now difficult to specify the states for this case of learning system optimization.
It is important to distinguish whether a unit is learning or teaching, how many students it has, or how many of its own people are being taught.
The question of whether you care about which students a teacher has becomes more difficult.
If the teachers are at the same level, it generally doesn't matter who teaches which student.
Unfortunately, this is not practical, as each teacher can only have one student who is taught by several teachers (namely the last one), unless you specify all students for each teacher, but we don't want that either (but it would probably work on the server side).

When constructing the states, you have to be careful not to produce two comparable states, as this can make the search space much larger.
Unfortunately, this happens very often, as it is not uncommon for there to be several equally good and equally large teaching units.
It helps here to only allow such teachers in a defined order.
Of course, such units should be taught in exactly the reverse order if possible.

What you quickly notice is that the number of states (i.e. possible combinations) grows exponentially.
Without A*-Search a result would be unthinkable.
Unfortunately, the A*-Searching for more than 10 units still takes quite a long time, you let them search for the very best target state.

Only by "blinders" did I manage to get the algorithm to a very good result in a reasonable amount of time.
This result often corresponds to the optimum.
In some cases, however, the algorithm misses opportunities.
This has to do with the construction mechanism of the states.
I don't create all possible combinations for a teacher to teach students, but only those in which the next free units are searched top-down.
This generally works quite well, but in exceptional cases a better condition is “overlooked”.

## Static learning chains

So far we have discussed how to schedule existing units as teachers/students.
Now it's about which unit structure you should form so that teaching and learning can be coordinated as well as possible.
Some typical teacher-student chains are presented and discussed below:

### Typical learning chains

- **Simple teacher-student chain** --consisting of a teacher unit (L) and a student unit (S) with 10*|L|=|S|.
  The teachers learn until they are two talent levels ahead, then they teach the students.
  When students are not studying, they do other activities.
  Disadvantage: slow learning pace, advantages: only two units are required, easy to automate.
  Useful for units where learning is not a priority, e.g. for miners who mainly only learn to reach deeper ore layers, or for tax collectors who gradually increase their combat skills in order to be able to fight smaller groups of monsters independently.
- **Pyramid** --Further development of the simple teacher-student chain, consisting of a teacher unit (L) and several layers of student units (S1, S2,...) with 10*|L|=|S1|, 10*|S1|=|S2|... 
  If the aim is to minimize costs when learning [expensive talents], then the teacher learns and then teaches the first student unit (S1).
  These then teach S2 etc. Students only learn when they are taught.
  Although this minimizes costs, it is faster if the students in the intermediate shifts learn even if they do not have a teacher.
  However, it doesn't make sense if that too*lowest*Student shift learns without a teacher.
  In the medium term, this will mean that there will be almost no teaching at all, because no layer will be able to achieve a talent advantage over the next lower level.
  If you want, you can skip the whole pyramid structure and just have a unit learn without a teacher.
  The more layers a pyramid has, the faster it learns.
  Since the number of people required increases by a factor of 10 with each shift, there are limits to the height of the pyramid.
- **Pyramid with double peak** --The teacher unit at the top of a pyramid learns at least two-thirds of the time and can teach at most one-third of the time. 
  However, it would be ideal if the first student unit learned half of the time (and passed on their knowledge in the other half).
  This leads to the idea of ​​using not just one teacher unit at the top but two.
  The hope that two teachers could then take turns teaching two-thirds of the time turns out to be deceptive.
  But you can achieve an increase in learning speed.
  More detailed analyzes show that a pyramid with a double top achieves the same learning speed as a normal pyramid that has one more layer.
  The pyramid with a double top is somewhat less efficient (i.e. people have relatively less time to do anything other than study), but it works with fewer people.
- **Pyramid of 5** --The 5 pyramid works as the name suggests with a factor of 5 in unit sizes. 
  In return, a teacher always teaches 2 units and thus has 10 times the number of students.
  This system can be staggered over any number of levels.
  The top level ideally has 6 units of the same size.
  The second level has 3 units of 5 times the size, the third level has 3 units of 25 times the size.
  One unit teaches each of the intermediate levels and two are taught.
  At the top level, one person teaches and the other 5 units learn without a teacher, but with brain power and/or an academy.
- **Learning from two talents** --Combat units (S) usually learn two talents, their [Weapon Talent and Stamina]. 
  It also turns out to be useful for various teachers (L_K,L_A) to use.
  In principle you have two options: The teachers are specialists and only learn one talent.
  Although this is better in terms of learning speed, such specialists are very vulnerable (or unusable) in the event of a fight.
  Alternatively, choose |S|=9*|L_K|=9*|L_A|.
  L_K learns the combat talent and then teaches S and L_A
  L_A learns endurance and then teaches S and L_K
- Pyramids with two talents --There are countless possible combinations here. 
  The greatest learning speeds are achieved when all but the lowest layer are doubled, e.g. L_K,L_A,S1_K,S1_A,S2_K,S2_A,S3.
  Of course, you also need a lot of units for this.

### Lernketten-Analyse

Four factors play a role when assessing a learning chain: Which one*Speed*is she learning (measured in learning attempts/week)? Like*effective*is it, i.e. how much time do people have to do something other than study? How many*Units*do you need? How many*people*do you need?
Young parties, for example, cannot build five-tier pyramids because they don't have that many people.
Older parties have to simplify their chains because of the unit limit.
Production units want to have a lot of time to work and only learn when it is really worth it, etc. With a few simplifications and a little mathematics, you can easily analyze learning chains regarding these four factors.

 **Simplifications:** 

1. All units take the same amount of time to reach the next level.
    In fact, there are random fluctuations in the learning time to the next level and teachers have to learn slightly more than students because they are at a higher talent level.
2. Time can be divided into any fine detail.
    In fact, you can only teach weekly./cmd-learn.md.
    In practice, this division is also fine enough.
3. “Teaching” and “being taught” do not interfere with each other.
    Situations such as: S2 could learn from S1, but also teach S3; S1 cannot learn from L and S3 cannot teach S4.
    Since S2 cannot do both at the same time, either S1 or S3 has to learn without a teacher, wasting time.
    In fact, such situations can (almost) only occur in the starting phase.
    In order for such a constellation to arise "on its own", S1 would have to have climbed two talent levels in a week, which is rather unlikely.

 **Example calculation**  
 for a pyramid with three levels (L,S1,S2): for each unit it is indicated what proportion of its time it spends being taught /learning without a teacher /teaching /doing something else.

- L cannot be taught
    Let the proportion of time in which L learns be x.
    So he teaches 1-x.
    Result:[0/x/1-x/0].
- S1 is taught 1-x by L and learns y without a teacher.
    In order to learn as quickly as L, you have to do 2*(1-x)+y=x.
    So y=3*x-2.
    The rest of the time[1-(1-x)-(3x-2)=2-2x]teaches S1.
    Yields[1-x /3x-2 /2-2x /0].
- S2 is taught 2-2x by S1, the rest of the time (1-(2-2x)=2x-1) he does something else.
    Yields[2-2x /0 /0 /2x-1].
- In order for everyone to learn at the same speed, x = 2*(2-2x), so x=4/5.
- So the learning speed is 4/5
- The time not used for learning (weighted by unit size) is (100*3/5+10*0+1*0)/111=0.540540...
  Three units and 111 people are required
  Below we specify this as a 4-tuple (0.8000, 0.5405, 3, 111).

In comparison, the same calculation assuming that each layer has to learn 10% less than the next higher level.

- L cannot be taught. 
  Let the proportion of time in which L learns be x.
  So he teaches 1-x.
  Result:[0/x/1-x/0].
- S1 is taught 1-x by L and learns y without a teacher. 
  Since S1 has to learn 10% less than L, the following applies: 2*(1-x)+y= 0.9x .
  So y=2.9x-2.
  The rest of the time[1-(1-x)-(2.9x-2)=2-1.9x]teaches S1.
  Yields[1-x /2.9x-2 /2-1.9x /0].
- S2 is taught 2-1.9x by S1 the rest of the time (1-(2-1.9x)=1.9x-1) he does something else. 
  Yields[2-1.9x /0 /0 /1.9x-1].
- So that S2 0.9*0.9=0.81 times as fast as L learns, must be 0.81x = 2*(2-1.9x), so x=0.8677. 
  So the learning speed of L is 0.8677, that of S1 is 0.7809 and that of S2 is 0.7028.
  On average that's 0.7113.
  The time not used for learning (weighted by unit size) is (100*0.6486+10*0+1*0)/111=0.5843.

You can see a clear difference in the calculated learning speed (0.7113 to 0.8000).
The absolute size of the values ​​given below should not be taken lightly.
The comparison between each other is more interesting (A is faster than B)

Now here's one **Overview of the learning chain analysis** for the above examples.

- L-S chain (pyramid with 2 layers): (0.6667, 0.6061, 2, 11) 
- Pyramid with 3 layers, the intermediate layer does not learn without a teacher: (0.6667, 0.6306, 3, 111). 
  With each additional shift, the proportion of time not spent studying approaches 0.6333.
  The learning speed remains the same.
- Pyramid with 3 layers, the intermediate layer learns even without a teacher: (0.8000, 0.5405, 3, 111). 
- Pyramid with 4 layers, the intermediate layers learn even without a teacher: (0.8571, 0.5143, 4, 1111). 
- Pyramid with 5 layers, the intermediate layers learn even without a teacher: (0.8889, 0.5000, 5, 11111). 
- Pyramid with 2 layers and double tip: (0.8000, 0.5000, 3, 12). 
  Additional peaks act similar to additional layers in a pyramid.
  The efficiency is slightly lower, fewer people are needed.
- Two teachers (for different talents) each teaching the other and a student unit: (1.0000, 0.4091, 3, 11). 
- Two teachers (for different talents) who each only teach the student unit: (1.2222, 0.2778, 3, 12). 
  The students learn at a speed of 4/3, the teachers only at 2/3.
- If three teachers teach three different talents, then the students can (almost) always learn with the teacher. 
  Unfortunately, there are only a few cases in which you want to learn three talents permanently.

### Other influences on speed

The above analyzes show how you can get more time out of 100% time by using the lessons and usually accepting a reduction in the learning speed.
For certain talents, however, it is extremely important to master them as well as possible and still be able to teach enough students.
The aim is therefore to increase the learning speed above 100% (= always learn without a teacher).

The increase through academy and brain wax are known.
They each have a 1/3 effect when learning without a teacher, i.e. both together result in a learning speed of 166%.

Other influencing factors that increase the maximum learning speed are races, terrain and familiars.
This takes advantage of the fact that talent fluctuates depending on the "condition" and that by changing the condition, a unit can become from teacher to student.
The best example of this are insects, which can push every talent in combination with other breeds.

Without going into too much detail, we note that the maximum learning speed of the best units can be over 100%.
The above considerations must therefore be expanded.

#### 5 pyramid

Let's assume an academy and brainpower for the 6 teacher units.
So we get 5/3=166%.
When teaching there is no learning progress (students not in the academy) therefore 0/3 = 0% in this case.
A teacher teaches, 5 learning -> 1/6*0/3 + 5/6*5/3= 0 + 25/18 = 139%.
The next level with 3 teaching units is divided into 2 learning and 1 teaching: 2/3*6/3 + 1/3*0% = 4/3 = 133% This is slightly slower, but ultimately faster because each level has about 10% less to learn, as mentioned above.
1-2 more such intermediate levels are possible, each increasing the number of possible students fivefold.

If you start with two units at the top, they will fill half of an academy -but they also require a lot of brain power.
The first intermediate level then has 3 units with 10 people each, the second has 3 units with 50 people each.
The third and probably last intermediate level has 250 people per unit and can therefore train 2500 people at once -at 200%, i.e. the students catch up.
Otherwise there would be 3750 that can be taught up to 133%.
i.e. after deducting a few percentages for the level differences, 4000 students should be possible.

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Lernketten&oldid=3553] -->

[teurer Talente]: ./skills.md
[Waffentalent und Ausdauer]: ./skills-list.md

#!/usr/bin/env python
# coding: utf-8

# In[178]:


var('x01,x10,x02,x20,x03,x30,x12,x21,x13,x31,x14,x41,x42,x04,x40,x23,x32,x34,x43,x45');


# In[2]:


adj= matrix([[1,x01,x02,0,x04],[x01,1,0,0,0],[x02, 0, 1, x23, 0],[0, 0, x23, 1, 0],[x04, 0, 0, 0, 1]])


# In[3]:


adj


# In[4]:


adj.det()


# In[5]:


adj.delete_rows([2]).delete_columns([3]).det()


# In[123]:


dgpat=DiGraph({0:[1, 2, 4],1:[0],2:[0,3],3:{2},4:{0}});dgpat


# In[6]:


pat=matrix([[1,x01,x02,x02*x23,x04],
            [x01,1,x01*x02,x01*x02*x23,x01*x04],
            [x02,x02*x01,1,x23,x02*x04],
            [x02*x23,x01*x02*x23,x23,1,x23*x02*x04],
            [x04,x04*x01,x04*x02,x04*x02*x23,1]]); pat


# In[7]:


pat.delete_rows([1]).delete_columns([2]).det()


# In[8]:


pat.delete_rows([2]).delete_columns([3]).det()


# In[9]:


pat.det()


# In[10]:


pat.delete_rows([0]).delete_columns([3]).det()


# In[11]:


pat.delete_rows([1]).delete_columns([2]).det()


# In[12]:


pat.delete_rows([1]).delete_columns([3]).det()


# In[13]:


pat.delete_rows([1]).delete_columns([3]).det()


# In[14]:


pat.delete_rows([2]).delete_columns([4]).det()


# In[15]:


pat.delete_rows([3]).delete_columns([4]).det()


# In[16]:


expand(pat.delete_rows([0]).delete_columns([1]).det()/x01)


# In[17]:


expand(pat.delete_rows([0]).delete_columns([2]).det()/x02)


# In[18]:


expand(-pat.delete_rows([2]).delete_columns([3]).det()/x23)


# In[19]:


expand(pat.delete_rows([0]).delete_columns([4]).det()/x04)


# In[142]:


patall=matrix([[1,x01,x02,x02*x23,x04],
            [x10,1,x10*x02,x10*x02*x23,x10*x04],
            [x20,x20*x01,1,x23,x20*x04],
            [x20*x32,x01*x20*x32,x32,1,x32*x20*x04],
            [x40,x40*x01,x40*x02,x40*x02*x23,1]]); table(patall)


# In[145]:


expand(patall.delete_rows([2]).delete_columns([3]).det()/x32)


# In[125]:


dgdpat=DiGraph({0:[1,2,4],1:[],2:[3],3:[],4:[]}); dgdpat


# In[20]:


dpat=matrix([[1,x01,x02,x02*x23,x04],
            [0,1,0,0,0],
            [0,0,1,x23,0],
            [0,0,0,1,0],
            [0,0,0,0,1]]); dpat


# In[21]:


dpat.delete_rows([1]).delete_columns([0]).det()


# In[22]:


dpat.delete_rows([3]).delete_columns([0]).det()


# In[23]:


dpat.delete_rows([4]).delete_columns([0]).det()


# In[24]:


dpat.delete_rows([2]).delete_columns([0]).det()


# In[25]:


dpat.delete_rows([0]).delete_columns([1]).det()


# In[26]:


dpat.det()


# In[27]:


dpat.delete_rows([0]).delete_columns([3]).det()


# In[126]:


dgdpat2=DiGraph({0:[1],1:[2],2:[]}); dgdpat2


# In[28]:


dpat2=matrix([[1,x01,x01*x12],[0,1,x12],[0,0,1]]); dpat2


# In[127]:


dgpat2=DiGraph({0:[1],1:[0,2],2:[1]}); dgpat2


# In[29]:


pat2=matrix([[1,x01,x01*x12],[x10,1,x12],[x21*x10,x21,1]]); pat2


# In[30]:


pat2.delete_rows([0]).delete_columns([2]).det()


# In[31]:


pat2.delete_rows([0]).delete_columns([2])


# In[32]:


pat2.delete_rows([2]).delete_columns([0])


# In[33]:


pat3=matrix([[1,x01,x01*x12,x01*x12*x23],[x10,1,x12,x12*x23],[x21*x10,x21,1,x23],[x32*x21*x10,x32*x21,x32,1]]); pat3


# In[34]:


pat3.delete_rows([3]).delete_columns([0])


# In[35]:


pat3.delete_rows([1]).delete_columns([0])


# In[36]:


expand(det(_)/x01)


# In[37]:


pat3.delete_rows([2]).delete_columns([1])


# In[38]:


expand(det(_)/x12)


# In[128]:


dgdcyc=DiGraph({0:[1],1:[2],2:[0]}); dgdcyc


# In[39]:


dcyc=matrix([[1,x01,x01*x12],[x12*x20,1,x12],[x20,x20*x01,1]])


# In[40]:


dcyc.delete_rows([0]).delete_columns([0]).det()


# In[41]:


dcyc.delete_rows([0]).delete_columns([1]).det()


# In[42]:


dcyc.delete_rows([0]).delete_columns([2]).det()


# In[43]:


dcyc.delete_rows([1]).delete_columns([0]).det()


# In[44]:


dcyc.delete_rows([1]).delete_columns([1]).det()


# In[45]:


dcyc.delete_rows([1]).delete_columns([2]).det()


# In[46]:


dcyc.delete_rows([2]).delete_columns([0]).det()


# In[47]:


dcyc.delete_rows([2]).delete_columns([1]).det()


# In[48]:


dcyc.delete_rows([2]).delete_columns([2]).det()


# In[129]:


dgdpats=DiGraph({0:[1,2],1:[3],2:[3],3:[]}); dgdpats


# In[49]:


dpats=matrix([[1,x01,x02,x01*x13+x02*x23],
              [0,1,0,x13],
              [0,0,1,x23],
              [0,0,0,1]]); table(dpats)


# In[50]:


dpats.delete_rows([]).delete_columns([]).det()


# In[51]:


dpats.delete_rows([3]).delete_columns([0]).det()


# In[52]:


dpats.delete_rows([2]).delete_columns([0]).det()


# In[53]:


dpats.delete_rows([1]).delete_columns([0]).det()


# In[54]:


dpats.delete_rows([0]).delete_columns([3]).det()


# In[55]:


dpats.delete_rows([3]).delete_columns([1]).det()


# In[56]:


dpats.delete_rows([3]).delete_columns([2]).det()


# In[133]:


dgdpats5=DiGraph({0:[1,2],1:[2,3],2:[1,3],3:[]});dgdpats5


# In[134]:


dpats5=matrix([[1,x01+x02*x21,x01*x12+x02,x02*x23+x01*x13+x01*x12*x23+x02*x21*x13],
               [0,1,x12,x13+x12*x23],
               [0,x21,1,x23+x21*x13],
               [0,0,0,1]]); table(dpats5)


# In[135]:


dpats5.delete_rows([]).delete_columns([]).det()


# In[137]:


expand(dpats5.delete_rows([2]).delete_columns([0]).det()/x02)


# In[138]:


expand(dpats5.delete_rows([3]).delete_columns([0]).det()/x03)


# In[111]:


dpatsall=matrix([[1,x01+x02*x21,x01*x12+x02,x02*x23+x01*x13+x01*x12*x23+x02*x21*x13],
               [0,1,x12,x13+x12*x23],
               [0,x21,1,x23+x21*x13],
               [0,0,0,1]]); table(dpatsall)


# In[112]:


expand(dpatsall.delete_rows([3]).delete_columns([0]).det())


# In[114]:


expand(dpatsall.delete_rows([2]).delete_columns([0]).det()/x02)


# In[115]:


expand(dpatsall.delete_rows([1]).delete_columns([0]).det()/x01)


# In[116]:


expand(dpatsall.delete_rows([3]).delete_columns([1]).det()/x13)


# In[117]:


expand(dpatsall.delete_rows([2]).delete_columns([1]).det()/x12)


# In[119]:


expand(dpatsall.delete_rows([3]).delete_columns([2]).det()/x23)


# In[140]:


dgthree=DiGraph({0:[1,2],1:[2]});dgthree


# In[120]:


three=matrix([[1,x01,x01*x12+x02],[0,1,x12],[0,0,1]]); table(three)


# In[121]:


three.delete_rows([2]).delete_columns([0]).det()


# In[141]:


dgdpats6=DiGraph({0:[1,2],1:[2],2:[3],3:[]});dgdpats6


# In[103]:


dpats6=matrix([[1,x01,x02+x01*x12,x02*x23+x01*x12*x23],
               [0,1,x12,x12*x23],
               [0,0,1,x23],
               [0,0,0,1]]); table(dpats6)


# In[109]:


expand(dpats6.delete_rows([3]).delete_columns([0]).det())


# In[110]:


expand(dpats6.delete_rows([2]).delete_columns([0]).det())


# In[146]:


dgpuz=DiGraph({0:[1],1:[2,3],2:[],3:[1]}); dgpuz


# In[151]:


puz=matrix([[1, x01, x01*x12, x01*x13],
            [0, 1, x12, x13],
            [0, 0, 1, 0],
            [0,x31,x31*x12, 1]]);table(puz)


# In[153]:


puz.delete_rows([2]).delete_columns([0]).det()


# In[154]:


expand(_)


# In[155]:


why=puz.delete_rows([2]).delete_columns([0]); why


# In[156]:


dgpuz2=DiGraph({0:[1],1:[2,3],2:[],3:[4],4:[1]}); dgpuz2


# In[165]:


puz2=matrix([[1,x01,x01*x12,x01*x13,x01*x13*x34],
            [0,1,x12,x13,x13*x34],
            [0,0,1,0,0],
            [0,x34*x41,x34*x41*x12,1,x34],
            [0,x41,x41*x42,x41*x43,1]]);table(puz2)


# In[166]:


expand(puz2.delete_rows([2]).delete_columns([0]).det())


# In[168]:


table(puz2.delete_rows([2]).delete_columns([0]))


# In[174]:


dglists={0:[1],1:[2],2:[3],3:[1,4],4:[2,5],5:[]}; dglists


# In[176]:


dg6=DiGraph(dglists);dg6


# In[191]:


dg6.all_paths(3,2)


# In[186]:


mdg6=matrix([[1, x01,         x01*x12,          x01*x12*x23, x01*x12*x23*x34, x01*x12*x23*x34*x45 ],
             [0, 1,           x12,              x12*x23,     x12*x23*x34,     x12*x23*x34*x45     ],
             [0, x23*x31,     1,                x23,         x23*x34,         x23*x34*x45         ],
             [0, x31,         x31*x12+x34*x42 , 1,           x34,             x34*x45             ],
             [0, x42*x23*x31, x42,              x42*x23,     1,                x45                ],
             [0, 0,           0,                0,           0,               1                   ]    ]);table(mdg6)


# In[187]:


expand(mdg6.delete_rows([5]).delete_columns([0]).det())


# In[188]:


table(mdg6.delete_rows([5]).delete_columns([0]))


# In[231]:


dg6.all_paths(3,2)


# In[198]:


'x' + str(3)


# In[200]:


toVar(3,4)


# In[208]:


from sage.misc.parser import Parser; myParser=Parser(make_var=var)


# In[209]:


myParser.parse('x34')


# In[211]:


def toVar(i,j):
    return( myParser.parse('x'+str(i)+str(j)))
    


# In[225]:


def listToMonomial(l):
    if (len(l)==1):
        return 1
    if (len(l)==0):
        raise Exception("Dont call this on 0 length lists")
    return toVar(l[0],l[1])*listToMonomial(l[1:])


# In[229]:


def listOfPathsToPolynomial(lp):
    if (len(lp)==0):
        return 0
    return ( listToMonomial(lp[0]) + listOfPathsToPolynomial(lp[1:]))


# In[232]:


listOfPathsToPolynomial(dg6.all_paths(3,2))


# In[250]:


def makePM(dig):
    return matrix(dig.num_verts(), lambda r,c: listOfPathsToPolynomial(dig.all_paths(r,c)))   


# In[251]:


table(makePM(dg6))


# In[252]:


thru0dig = DiGraph({0:[1], 1:[2,3], 2:[0], 3:[]});thru0dig


# In[253]:


thru0PM = makePM(thru0dig); table(thru0PM)


# In[255]:


expand(thru0PM.delete_rows([3]).delete_columns([0]).det())


# In[256]:


table(thru0PM.delete_rows([3]).delete_columns([0]))


# In[261]:


thru0dig1 = DiGraph({0:[1,3], 1:[2,3], 2:[0], 3:[]});thru0dig1


# In[262]:


thru0dig1PM=makePM(thru0dig1);table(thru0dig1PM)


# In[264]:


expand(thru0dig1PM.delete_rows([3]).delete_columns([0]).det()/x03)


# In[266]:


k6 = DiGraph({0:[1,2,3,4],
              1:[0,2,3,4,5],
              2:[0,1,3,4,5],
              3:[0,1,2,4,5],
              4:[0,1,2,3,5],
              5:[0,1,2,3,4]}); k6


# In[268]:


k6mat=makePM(k6);table(k6mat)


# In[269]:


k6mat


# In[270]:


k6mat50=k6mat.delete_rows([5]).delete_columns([0])


# In[1]:


#bigd=det(k6mat)


# In[272]:


k6c = DiGraph({0:[1,2,3,4],
              1:[2,3,4,5],
              2:[3,4,5],
              3:[4,5],
              4:[5],
              5:[0,1,2,3,4]}); k6c


# In[273]:


k6cm = makePM(k6c)


# In[274]:


k6cm


# In[276]:


k6cm05=k6cm.delete_rows([5]).delete_columns([0])


# In[277]:


bigd1=det(k6cm05)


# In[279]:


expand(bigd1)


# In[282]:


tryg=DiGraph({0:[1,2],
              1:[0,2,5],
              2:[3],
              3:[4],
              4:[5],
              5:[0]});tryg


# In[283]:


trygm = makePM(tryg);table(trygm)


# In[284]:


trygm05=trygm.delete_rows([5]).delete_columns([0]);table(trygm05)


# In[285]:


expand(det(trygm05))


# In[286]:


probd=_


# In[287]:


probd


# In[295]:


expand(probd/(x01*x02*x15*x50*x45*x34*x23))


# In[296]:


badg=DiGraph({0:[1,2], 1:[5],2:[3],3:[4],4:[5],5:[0]});badg


# In[298]:


sbadg=DiGraph({0:[1,2],2:[3],1:[3],3:[0]});sbadg


# In[300]:


sbadgm=makePM(sbadg);table(sbadgm)


# In[314]:


sbadgm03=sbadgm.delete_rows([3]).delete_columns([0]);table(sbadgm03)


# In[315]:


sbadgmdet=sbadgm03.det();sbadgmdet


# In[316]:


expand(sbadgmdet)


# In[309]:


expand((sbadgmdet)/(x01*x02*x13*x23*x30))


# In[330]:


sbadg34=DiGraph({0:[1,2],2:[3],1:[4],3:[4],4:[0]});sbadg34


# In[331]:


sbadg34PM=makePM(sbadg34);table(sbadg34PM)


# In[334]:


sbadg34det=expand(sbadg34PM.delete_rows([4]).delete_columns([0]).det());sbadg34det


# In[335]:


expand(sbadg34det/(x01*x02*x14*x23*x34*x40))


# In[310]:


sillyg=DiGraph({0:[1],1:[2],2:[0]}); sillyg


# In[311]:


sillygPM=makePM(sillyg);sillygPM


# In[313]:


sillysubmatrix=sillygPM.delete_rows([2]).delete_columns([0]);sillysubmatrix


# In[320]:


sbadg4=DiGraph({0:[1,2],2:[3],1:[3],3:[0,4]});sbadg4


# In[321]:


sbadg4PM=makePM(sbadg4);table(sbadg4PM)


# In[323]:


expand(sbadg4PM.delete_rows([4]).delete_columns([0]).det())


# In[324]:


sbadg44=DiGraph({0:[1,2],2:[3],1:[3],3:[0],4:[0]});sbadg44


# In[325]:


sbadg44PM=makePM(sbadg44);sbadg44PM


# In[326]:


expand(sbadg44PM.delete_rows([3]).delete_columns([4]).det())


# In[336]:


Jul1Dig=DiGraph({0:[1,2],1:[3],2:[4],3:[2,5],4:[5]});Jul1Dig


# In[337]:


Jul1PM=makePM(Jul1Dig);table(Jul1PM)


# In[339]:


expand(Jul1PM.delete_rows([5]).delete_columns([0]).det())


# In[340]:


Jul1Dig2=DiGraph({0:[1,2],1:[3],2:[4],3:[0,2,5],4:[5],5:[2]});Jul1Dig2


# In[341]:


Jul1Dig2PM=makePM(Jul1Dig2);table(Jul1Dig2PM)


# In[342]:


expand(Jul1Dig2PM.delete_rows([5]).delete_columns([0]).det())


# In[343]:


Jul1Dig3=DiGraph({0:[1,2],1:[3],2:[4],3:[0,2,5],4:[5],5:[3]});Jul1Dig3


# In[344]:


Jul1Dig3PM=makePM(Jul1Dig3);table(Jul1Dig3PM)


# In[345]:


expand(Jul1Dig3PM.delete_rows([5]).delete_columns([0]).det())


# In[351]:


FromDig3=DiGraph({0:[1,2],1:[3],2:[4],3:[0,5],4:[5],5:[3]});FromDig3


# In[352]:


FromDig3PM=makePM(FromDig3);table(FromDig3PM)


# In[354]:


Dig3Ans=expand(FromDig3PM.delete_rows([5]).delete_columns([0]).det());Dig3Ans


# In[355]:


expand(Dig3Ans/(x01*x02*x13*x24*x30*x35*x45*x53))


# In[356]:


Dig4=DiGraph({0:[1,2],1:[3],2:[4],3:[0,4],4:[3]});Dig4


# In[358]:


Dig4PM=makePM(Dig4);table(Dig4PM)


# In[360]:


Dig4det=expand(Dig4PM.delete_rows([4]).delete_columns([0]).det());Dig4det


# In[362]:


expand(Dig4det/(x01*x02*x13*x24*x30*x34*x43))


# In[383]:


var('graph,det,n');
def retdic():
    return {n:1,graph:Dig4,det:Dig4det}


# In[386]:


retdic()[graph]


# In[425]:


var('graph,source,sink,PM,PMT,resultdet');
def doit(indg,src,sinkin):
    pm=makePM(indg)
    subpm=pm.delete_rows([sinkin]).delete_columns([src])
    ans=factor(expand(subpm.det()))
    display(indg)
    display(table(pm))
    display(table(subpm))
    display("Source="+str(src)+" Sink="+str(sinkin))
    display(ans)
    return {graph:indg, source:src, sink:sinkin,PM:pm,resultdet:ans}


# In[422]:


doit(Dig4,0,4)


# In[419]:


doit(Dig4,4,0)


# In[420]:


dgpat


# In[430]:


doit(dgpat,1,3)


# In[433]:


#help(DiGraph)


# In[473]:


tree7=DiGraph([[0,1],[1,0],[0,2],[2,0],[2,3],[3,2],[3,4],[4,3],[2,5],[5,2],[6,5],[5,6]],format='list_of_edges');tree7


# In[2]:


tree6=DiGraph([[1,0],[0,1],[1,2],[2,1],[2,3],[3,2],[1,4],[4,1],[4,5],[5,4]]);tree6


# In[474]:


tree7result=doit(tree7,0,5)


# In[475]:


newcounterex4=DiGraph([[0,1],[1,0],[1,3],[3,1],[0,2],[2,3]]);newcounterex4


# In[476]:


newcounterex4result=doit(newcounterex4,0,3)


# In[477]:


tree7result[PM]


# In[478]:


#cop=DiGraph(tree7result[PM]).copy(immutable=True);
#list(cop.all_paths_iterator([0],[5],simple=True,labels=False))
#We clearly get all permutations of all lengths that begin with 0 and end in 5, since all PM enties are \neq 0.


# In[485]:


tree4=DiGraph([[0,1],[1,0],[1,2],[2,1],[3,1],[1,3]])


# In[486]:


tree4result=doit(tree4,0,3)


# In[489]:


tree5=DiGraph([[0,1],[1,0],[1,2],[2,1],[4,1],[1,4],[2,3],[3,2]]);
tree5result=doit(tree5,0,4)


# ## Lemma 1 (Remove non-terminal leaf vertex, either adjacent or not adjacient to a terminal.)

# In[552]:


tree6=DiGraph([[0,1],[1,0],[1,2],[2,1],[2,3],[3,2],[1,4],[4,1],[4,5],[5,4]]);tree6


# In[560]:


doit(tree6,3,5);
result=doit(tree6,1,5)
tree6PM=result[PM]


# In[564]:


rowops=matrix([[1,-x01,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])
print(rowops);print('\n');
print(tree6PM);print('\n');
print(rowops*tree6PM)


# In[529]:


doit(tree5,0,1)


# In[490]:


tree5result2=doit(tree5,0,3)


# In[491]:


tree7result2=doit(tree7,1,6)


# In[492]:


piecegr1=DiGraph([[0,2],[1,0],[2,3],[3,4],[2,5],[3,2],[4,3],[5,6],[2,0],[5,2]]);piecegr1


# In[493]:


resultpiecegr1=doit(piecegr1,1,6)


# In[494]:


resultpiecegr1


# In[495]:


pm=resultpiecegr1[PM];pm


# In[500]:


x10=0;print(expand(pm));var('x10');


# In[501]:


x10


# In[508]:


var('x10')


# In[513]:


pm.subs(x10==0,x32==0,x43==0)


# In[517]:


Out[513].delete_rows([1,6]).delete_columns([1,6])


# In[521]:


mat=Out[517];mat


# In[523]:


mat.det()


# In[528]:


mat.delete_rows([2]).delete_columns([0])


# In[532]:


pathetic=DiGraph([[0,1],[1,0],[1,2],[2,1],[2,3],[3,2],[3,4],[4,3],[4,5],[5,4]])


# In[534]:


doit(pathetic,2,4)


# In[535]:


doit(pathetic,1,4)


# In[536]:


doit(pathetic,0,5)


# In[565]:


trigr=DiGraph([[0,2],[0,3],[2,4],[3,4],[4,1],[1,0]])


# In[567]:


doit(trigr,0,4)


# In[ ]:





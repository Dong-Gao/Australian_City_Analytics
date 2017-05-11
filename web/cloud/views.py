# Cluster and Cloud Computing
# Group Project
# Team 16
#
# Kaile Wei: 812381
# Nanjiang Li: 741524
# Hongzhen Xie: 773383
# Dong Gao: 795622
# Chuang Ying: 844566

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView

from django.shortcuts import render
from django.shortcuts import render_to_response
import json
import couchdb
# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"




def get_data3():
    server = couchdb.Server('http://localhost:5984/')
    db = server.create('test')

    results = db.view('designview1/newview')
    for row in results:
        dic = row.value
        print dic




class scenario_oneView(TemplateView):
    def get(self, request, **kwargs):
        data = emotionData()
        return render_to_response('scenario-one.html', {'my_data':json.dumps(data)})

class scenario_twoView(TemplateView):
    def get(self, request, **kwargs):
        data = culturalData()
        return render_to_response('scenario-two.html', {'my_data': json.dumps(data)})
                                 #template_name = "scenario-two.html"
class scenario_twoView2(TemplateView):
    def get(self, request, **kwargs):
        data = culturalData2()
        return render_to_response('scenario-two2.html', {'my_data': json.dumps(data)})

class scenario_threeView(TemplateView):
    def get(self, request, **kwargs):
       data = smokeData()

       return render_to_response('scenario-three.html', {'my_data': json.dumps(data)})

class scenario_threeView2(TemplateView):
    def get(self, request, **kwargs):
        data = smokeData2()
        return render_to_response('scenario-three2.html', {'my_data': json.dumps(data)})
    #template_name = "scenario-three.html"

class team_memberView(TemplateView):
    template_name = "team-member.html"
   # return render_to_response('reserve/templates/avail_times.html', {'courts': courts, 'club_name': club_name})


def emotionData():
       server = couchdb.Server('http://sourcead:iamfine@115.146.93.79:5984/')
       db = server['result']
       doc = db['emotionResult']

       data = [['Cities','Adelaide', 'Brisbane','Canberra','Darwin','Hobat','Melbourne','Perth','Sydney'],
                 ['00:00~05:59',  doc['Adelaide']['0-6']['score'],doc['Brisbane']['0-6']['score'],doc['Canberra']['0-6']['score'],doc['Darwin']['0-6']['score'],
                                  doc['Hobart']['0-6']['score'],doc['Melbourne']['0-6']['score'],doc['Perth']['0-6']['score'],doc['Sydney']['0-6']['score']],
                 ['06:00~11:59',  doc['Adelaide']['6-12']['score'],doc['Brisbane']['6-12']['score'],doc['Canberra']['6-12']['score'],doc['Darwin']['6-12']['score'],
                                  doc['Hobart']['6-12']['score'],doc['Melbourne']['6-12']['score'],doc['Perth']['6-12']['score'],doc['Sydney']['6-12']['score']],
                 ['12:00~17:59',  doc['Adelaide']['12-18']['score'],doc['Brisbane']['12-18']['score'],doc['Canberra']['12-18']['score'],doc['Darwin']['12-18']['score'],
                                  doc['Hobart']['12-18']['score'],doc['Melbourne']['12-18']['score'],doc['Perth']['12-18']['score'],doc['Sydney']['12-18']['score']],
                 ['18:00~23:59',  doc['Adelaide']['18-24']['score'],doc['Brisbane']['18-24']['score'],doc['Canberra']['18-24']['score'],doc['Darwin']['18-24']['score'],
                                  doc['Hobart']['18-24']['score'],doc['Melbourne']['18-24']['score'],doc['Perth']['18-24']['score'],doc['Sydney']['18-24']['score']],
        ]
       return data

def culturalData():
    server = couchdb.Server('http://sourcead:iamfine@115.146.93.79:5984/')
    db = server['result']
    doc = db['culture']
    #print doc
    data = [['State', 'City', 'Ra:(Mandarin Speaker Residents\' Rate)', 'Rb:(Twitters Mention Chinese Culture Rate\')'],
            ['AU-VIC', 'Melbourne',0.02412, round(1.0*doc['Melbourne']['match']/doc['Melbourne']['total'],5)],
            ['AU-NSW', 'Sydney', 0.02899,round(1.0*doc['Sydney']['match']/doc['Sydney']['total'],5)],
            ['AU-QLD', 'Brisbane',0.01434, round(1.0*doc['Brisbane']['match']/doc['Brisbane']['total'],5)],
            ['AU-SA', 'Adelaide', 0.01261,round(1.0*doc['Adelaide']['match']/doc['Adelaide']['total'],5)],
            ['AU-TAS', 'Hobart',0.00699, round(1.0*doc['Hobart']['match']/doc['Hobart']['total'],5)],
            ['AU-ACT', 'Canberra',0.01814, round(1.0*doc['Canberra']['match']/doc['Canberra']['total'],5)],
            ['AU-NT', 'Darwin',0.00809, round(1.0*doc['Darwin']['match']/doc['Darwin']['total'],5)],
            ['AU-WA', 'Perth',0.01458, round(1.0*doc['Perth']['match']/ doc['Perth']['total'],5)],
            ]
    #print data
    return data


def culturalData2():

    server = couchdb.Server('http://sourcead:iamfine@115.146.93.79:5984/')
    db = server['result']
    doc = db['culture']
    # print doc
    data = [['City', 'Ra:(Mandarin Speaker Residents\' Rate)', 'Rb:(Twitters Mention Chinese Culture\' Rate)'],
            [ 'Melbourne', 0.02412, round(1.0*doc['Melbourne']['match']/doc['Melbourne']['total'],5)],
            [ 'Sydney',0.02899, round(1.0*doc['Sydney']['match']/doc['Sydney']['total'],5)],
            [ 'Brisbane', 0.01434,round(1.0*doc['Brisbane']['match']/doc['Brisbane']['total'],5)],
            [ 'Adelaide',0.01261, round(1.0*doc['Adelaide']['match']/doc['Adelaide']['total'],5)],
            [ 'Hobart', 0.00699,round(1.0*doc['Hobart']['match']/doc['Hobart']['total'],5)],
            [ 'Canberra',0.01814, round(1.0*doc['Canberra']['match']/doc['Canberra']['total'],5)],
            [ 'Darwin', 0.00809,round(1.0*doc['Darwin']['match']/doc['Darwin']['total'],5)],
            [ 'Perth', 0.01458,round(1.0*doc['Perth']['match']/doc['Perth']['total'],5)],
            ]
    return data


def smokeData():
    server = couchdb.Server('http://sourcead:iamfine@115.146.93.79:5984/')
    db = server['result']
    doc = db['smokeResult']
    data = [['State','City','Positive','Negativce'],
        ['AU-VIC', 'Melbourne',doc['Melbourne']['positive'], doc['Melbourne']['negative']],
        ['AU-NSW', 'Sydney', doc['Sydney']['positive'], doc['Sydney']['negative']],
        ['AU-QLD', 'Brisbane',doc['Brisbane']['positive'], doc['Brisbane']['negative']],
        ['AU-SA', 'Adelaide', doc['Adelaide']['positive'], doc['Adelaide']['negative']],
        ['AU-TAS', 'Hobart', doc['Hobart']['positive'], doc['Hobart']['negative']],
        ['AU-ACT', 'Canberra', doc['Canberra']['positive'], doc['Canberra']['negative']],
        ['AU-NT', 'Darwin', doc['Darwin']['positive'], doc['Darwin']['negative']],
        ['AU-WA', 'Perth',doc['Perth']['positive'], doc['Perth']['negative']],
     ]
    return data


def smokeData2():
    server = couchdb.Server('http://sourcead:iamfine@115.146.93.79:5984/')
    db = server['result']
    doc = db['smokeResult']

    data = [['Cities', 'Female Population Rate(%)', 'Negative Attitude Rate(‰)'],
            ['Brisbane', doc['Brisbane']['female_rate']*100, doc['Brisbane']['rate']*1000],
            ['Sydney', doc['Sydney']['female_rate']*100, doc['Sydney']['rate']*1000],
            ['Melbourne', doc['Melbourne']['female_rate']*100, doc['Melbourne']['rate']*1000],
            ['Canberra', doc['Canberra']['female_rate']*100, doc['Canberra']['rate']*1000],
            ['Adelaide', doc['Adelaide']['female_rate']*100, doc['Adelaide']['rate']*1000],
            ['Perth', doc['Perth']['female_rate']*100, doc['Perth']['rate']*1000],
            ['Hobart', doc['Hobart']['female_rate']*100, doc['Hobart']['rate']*1000],
            ['Darwin', doc['Darwin']['female_rate']*100, doc['Darwin']['rate']*1000],
            ]
    return data

__version__ = '$Id$'

from Products.CMFPlone import utils
import DateTime
import pdb
import os
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from zope.interface import implements
from Products.Five.browser import BrowserView
class List(BrowserView):

			
	def __call__(self):
		context = aq_inner(self.context)
                #import pdb;pdb.set_trace()
                catalog = getToolByName(context, 'portal_catalog')
                idea=context.REQUEST.get('id', None)
                states=context.getState_source()
                state_list=[]
                for i in states:
                    ul_dict={}
                    ul_dict['len']=len(catalog(portal_type="kontratazioa", review_state="published", getState=i))
                    ul_dict['state']=i
                    state_list.append(ul_dict)
                dict={}
                if idea:
                   for obj in states:
                       if idea==obj:
                           dict[obj]="on"
                       else:
                           dict[obj]="off"
                else:
                   dict[states[0]]="on"
                   for obj in states[1:]:
                       dict[obj]="off"
                return [dict, state_list]

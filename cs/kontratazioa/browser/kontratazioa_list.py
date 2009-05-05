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
                idea=context.REQUEST.get('id', None)
                if not idea:
                    state_sources=context.getState_source()
                    if state_sources:
                        idea=state_sources[0]
                catalog = getToolByName(context, 'portal_catalog')
                organizations=catalog.uniqueValuesFor("getOrganization")
                publication_years=catalog.uniqueValuesFor("kontratazioa_publication_year")
                dict={}
                year_dict={}
                for year in publication_years:
                    for organization in organizations:
                        kontratazioak=catalog(portal_type="kontratazioa", review_state="published", getState=idea, getOrganization=organization)
                        if kontratazioak:
                            dict[organization]=kontratazioak
                    year_dict[year]=dict
                #import pdb;pdb.set_trace()
                return year_dict

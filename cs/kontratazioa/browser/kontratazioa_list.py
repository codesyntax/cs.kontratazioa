__version__ = '$Id$'

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
class List(BrowserView):

			
	def __call__(self):
                #import pdb;pdb.set_trace()
		context = aq_inner(self.context)
                catalog = getToolByName(context, 'portal_catalog')
                idea=context.REQUEST.get('id', None)
                if not idea:
                    state_sources=context.getState_source()
                    if state_sources:
                        idea=state_sources[0]

                year_dict={}
                if idea != context.getState_source()[-1]:
                    dict={}
                    
                    kontratazioak=catalog(portal_type="kontratazioa", review_state="published", getState=idea, sort_on="kontratazioa_contract_type")
                    if kontratazioak:
                            list(kontratazioak).sort(cmp=lambda x,y: cmp(x.Title, y.Title))
                            dict['kontratazioak']=kontratazioak
                    year_dict['denak']=dict
                    return year_dict
                
                publication_years=catalog.uniqueValuesFor("kontratazioa_publication_year")
                
               
                for year in publication_years:
                    dict={}
                    
                    kontratazioak=catalog(portal_type="kontratazioa", review_state="published", getState=idea, kontratazioa_publication_year=year, sort_on="kontratazioa_contract_type")
                    if kontratazioak:
                        list(kontratazioak).sort(cmp=lambda x,y: cmp(x.Title, y.Title))   
                        dict['kontratazioak']=kontratazioak
                    year_dict[year]=dict
                
                return year_dict

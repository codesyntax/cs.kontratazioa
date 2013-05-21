from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView


class List(BrowserView):

    def __call__(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        organizations = catalog.uniqueValuesFor("getOrganization")
        idea = self.request.get('id', None)
        if not idea:
            state_sources = context.getState_source()
            if state_sources:
                idea = state_sources[0]

        year_dict = {}
        if idea != context.getState_source()[-1]:
            dict = {}
            for organization in organizations:
                kontratazioak = catalog(portal_type="kontratazioa",
                                        review_state="published",
                                        getState=idea,
                                        getOrganization=organization,
                                        sort_on="kontratazioa_contract_type")
                if kontratazioak:
                    list(kontratazioak).sort(cmp=lambda x, y: cmp(x.Title, y.Title))
                    dict[organization] = kontratazioak
            year_dict['denak'] = dict
            return year_dict

        publication_years = catalog.uniqueValuesFor("kontratazioa_publication_year")

        for year in publication_years:
            dict = {}
            for organization in organizations:
                kontratazioak = catalog(portal_type="kontratazioa",
                                        review_state="published",
                                        getState=idea,
                                        getOrganization=organization,
                                        kontratazioa_publication_year=year,
                                        sort_on="kontratazioa_contract_type")
                if kontratazioak:
                    list(kontratazioak).sort(cmp=lambda x, y: cmp(x.Title, y.Title))
                    dict[organization] = kontratazioak

            year_dict[year] = dict

        return year_dict

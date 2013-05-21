from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class kontratazioaView(BrowserView):
    """
    kontratazioa browser view
    """

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

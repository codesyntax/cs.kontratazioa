from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class kontratazioaFolderView(BrowserView):
    """
    kontratazioaFolder browser view
    """

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

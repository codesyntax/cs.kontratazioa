"""Definition of the kontratazioaFolder content type
"""

from zope.interface import implements, directlyProvides
try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from cs.kontratazioa import kontratazioaMessageFactory as _
from cs.kontratazioa.interfaces import IkontratazioaFolder
from cs.kontratazioa.config import PROJECTNAME

kontratazioaFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.LinesField(
        name='contract_type',
        storage = atapi.AnnotationStorage(),
        required=False,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.LinesWidget(
            label=_(u"contract_type"),
            description=_(u"Description of contract_type"),
        ),
    ),
    atapi.LinesField(
        name='process',
        storage = atapi.AnnotationStorage(),
        required=False,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.LinesWidget(
            label=_(u"process"),
            description=_(u"Description of process"),
        ),
    ),
    atapi.LinesField(
        name='izapidea',
        storage = atapi.AnnotationStorage(),
        required=False,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.LinesWidget(
            label=_(u"izapidea"),
            description=_(u"Description of izapidea"),
        ),
    ),
    atapi.LinesField(
        name='organization_source',
        storage = atapi.AnnotationStorage(),
        required=False,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.LinesWidget(
            label=_(u"organization_source"),
            description=_(u"Description of organization_source"),
        ),
    ),
    atapi.LinesField(
        name='kontratazio_organoa',
        storage = atapi.AnnotationStorage(),
        required=False,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.LinesWidget(
            label=_(u"kontratazio_organoa"),
            description=_(u"Description of kontratazioa_organoa"),
        ),
    ),
     atapi.LinesField(
        name='state_source',
        storage = atapi.AnnotationStorage(),
        required=False,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.LinesWidget(
            label=_(u"state_source"),
            description=_(u"Description of state_source"),
        ),
    ),
    
    atapi.TextField('contact_information',
                        required=False,
                        searchable=True,
			storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'contact_information'),
                                                description=_(u'Description of contact_information'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),
))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

kontratazioaFolderSchema['title'].storage = atapi.AnnotationStorage()
kontratazioaFolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    kontratazioaFolderSchema,
    folderish=True,
    moveDiscussion=False
)

class kontratazioaFolder(folder.ATFolder):
    """Description of the Example Type"""
    implements(IkontratazioaFolder)

    meta_type = "kontratazioaFolder"
    schema = kontratazioaFolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(kontratazioaFolder, PROJECTNAME)

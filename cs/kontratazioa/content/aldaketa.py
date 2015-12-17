"""Definition of the Aldaketa content type
"""

from zope.interface import implements
try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Acquisition import aq_parent
from cs.kontratazioa import kontratazioaMessageFactory as _
from cs.kontratazioa.interfaces import IAldaketa
from cs.kontratazioa.config import PROJECTNAME


AldaketaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.DateTimeField(
        name='akordioaren_data',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"akordioaren_data"),
        ),
    ),

    atapi.FileField('akordioa',
                  searchable=1,
                  storage=atapi.AnnotationStorage(migrate=True),
                  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u'akordioa'),
                     ),
                  ),
    atapi.TextField('aldaketaren_zenbatekoa',
        required=False,
        searchable=True,
        storage=atapi.AnnotationStorage(),
        validators=('isTidyHtmlWithCleanup',),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'aldaketaren_zenbatekoa'),
                                rows=10,
                                allow_file_upload=False),
        ),

    

    atapi.DateTimeField(
        name='aldaketaren_data',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"aldaketaren_data"),
        ),
    ),

    
    
))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

AldaketaSchema['title'].storage = atapi.AnnotationStorage()
AldaketaSchema['description'].storage = atapi.AnnotationStorage()


class Aldaketa(folder.ATFolder):
    """Kontratazioan aldaketak gehitzeko elementua"""
    implements(IAldaketa)

    meta_type = "Aldaketa"
    schema = AldaketaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Aldaketa, PROJECTNAME)

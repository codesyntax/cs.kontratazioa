"""Definition of the kontratazioa content type
"""

from zope.interface import implements
try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Acquisition import aq_parent
from cs.kontratazioa import kontratazioaMessageFactory as _
from cs.kontratazioa.interfaces import Ikontratazioa
from cs.kontratazioa.config import PROJECTNAME

fields = folder.ATFolderSchema.copy().fields()

kontratazioaSchema = atapi.ManagedSchema((
    # -*- Your Archetypes field definitions here ... -*-
    atapi.StringField(
        name='file_number',
        required=False,
        languageIndependent=1,
        storage=atapi.AnnotationStorage(),
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.StringWidget(
            label=_(u"file_number"),
        ),
    ),
    atapi.StringField('contract_type',
                  searchable=1,
                  languageIndependent=0,
                  required=1,
                  vocabulary='selection_contract_type',
                  widget=atapi.SelectionWidget(
                     label=_(u'put_contract_type'),
                     ),
                  ),
    atapi.StringField('process',
                  searchable=1,
                  languageIndependent=0,
                  vocabulary='selection_process',
                  widget=atapi.SelectionWidget(
                     label=_(u'process'),

                     ),
                  ),
    atapi.StringField('izapidea',
                  searchable=1,
                  languageIndependent=0,
                  vocabulary='selection_izapidea',
                  widget=atapi.SelectionWidget(
                     label=_(u'izapidea'),

                     ),
                  ),
    atapi.StringField('organization',
                  searchable=1,
                                  languageIndependent=0,
                  required=True,
                  vocabulary='selection_organization',
                  widget=atapi.SelectionWidget(
                     label=_(u'organization'),

                     ),
                  ),
    atapi.StringField('kontratazio_organoa',
                  searchable=1,
                  languageIndependent=0,
                  vocabulary='selection_kontratazio_organoa',
                  widget=atapi.SelectionWidget(
                     label=_(u'put_kontratazio_organoa'),

                     ),
                  ),

    atapi.DateTimeField(
        name='published_date',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"published_date"),
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name='published_date_boletin',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"published_date_boletin"),
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name='organo_contratacion_date',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"organo_contratacion_date"),
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name='last_date',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"last_date"),
        ),
    ),

    atapi.DateTimeField(
        name='eskaintza_ekonomikoa_date',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"eskaintza_ekonomikoa_date"),
        ),
    ),
    atapi.DateTimeField(
        name='kontratuasinatu_date',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"Kontratua sinatzeko data"),
        ),
    ),
    atapi.StringField(
        name='lizitazio_aurrekontua',
        required=False,
        languageIndependent=0,
        storage=atapi.AnnotationStorage(),
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.StringWidget(
            label=_(u"lizitazio_aurrekontua"),
        ),
    ),
    atapi.TextField('documentation',
                        required=False,
                        searchable=True,
                        storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'put_documentation'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),

     atapi.FileField('attach1',
                  searchable=1,
                  languageIndependent=1,
                  storage=atapi.AnnotationStorage(migrate=True),
                  widget=atapi.FileWidget(
                     label=_(u'attach1'),
                     ),
                  ),

     atapi.TextField('attach1_information',
                    required=False,
                    searchable=True,
                    storage=atapi.AnnotationStorage(),
                    validators=('isTidyHtmlWithCleanup',),
                    default_output_type='text/x-html-safe',
                    widget=atapi.RichWidget(label=_(u'attach1_information'),
                                            rows=10,
                                            allow_file_upload=False),
                   ),
     atapi.FileField('attach2',
                  searchable=1,
                  storage=atapi.AnnotationStorage(migrate=True),
                  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u'attach2'),
                     ),
                  ),
     atapi.FileField('attach3',
                  searchable=1,
                  languageIndependent=1,
                  #storage = atapi.AnnotationStorage(migrate=True),
                  widget=atapi.FileWidget(
                     label=_(u'attach3'),
                     ),
                  ),

     atapi.FileField('attach4',
                  searchable=1,
                  storage=atapi.AnnotationStorage(migrate=True),
                  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u'attach4'),
                     ),
                  ),


    atapi.FileField('behin_behineko_file',
                  searchable=1,
                  storage=atapi.AnnotationStorage(migrate=True),
                  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u'behin_behineko_file'),
                     ),
                  ),

    atapi.DateTimeField(
        name='behin_behineko_adjudikazio_date',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"behin_behineko_adjudikazio_date"),
            show_hm=False,
        ),
    ),

    atapi.DateTimeField(
        name='behin_behineko_profile_date',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"behin_behineko_profile_date"),
            show_hm=False,
        ),
    ),

    atapi.TextField('behin_behineko_adjudikazioduna',
            required=False,
            searchable=True,
            storage=atapi.AnnotationStorage(),
            validators=('isTidyHtmlWithCleanup',),
            default_output_type='text/x-html-safe',
            widget=atapi.RichWidget(label=_(u'behin_behineko_adjudikazioduna'),
                                    rows=10,
                                    allow_file_upload=False),
            ),

    atapi.TextField('behin_behineko_adjudikazioaren_zenbatekoa',
        required=False,
        searchable=True,
        storage=atapi.AnnotationStorage(),
        validators=('isTidyHtmlWithCleanup',),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'behin_behineko_adjudikazioaren_zenbatekoa'),
                                rows=10,
                                allow_file_upload=False),
        ),

    atapi.FileField('behin_betiko_file',
                  searchable=1,
                  storage = atapi.AnnotationStorage(migrate=True),
                  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u'behin_betiko_file'),
                     ),
                  ),

    atapi.DateTimeField(
        name='behin_betiko_adjudikazio_date',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"behin_betiko_adjudikazio_date"),
            show_hm=False,
        ),
    ),

    atapi.DateTimeField(
        name='behin_betiko_profile_date',
        storage=atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"behin_betiko_profile_date"),
        ),
    ),
    atapi.TextField('behin_betiko_adjudikazioduna',
        required=False,
        searchable=True,
        storage=atapi.AnnotationStorage(),
        validators=('isTidyHtmlWithCleanup',),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'behin_betiko_adjudikazioduna'),
                                rows=10,
                                allow_file_upload=False),
        ),

    atapi.TextField('behin_betiko_adjudikazioaren_zenbatekoa',
        required=False,
        searchable=True,
        storage=atapi.AnnotationStorage(),
        validators=('isTidyHtmlWithCleanup',),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'behin_betiko_adjudikazioaren_zenbatekoa'),
                                rows=10,
                                allow_file_upload=False),
        ),

    atapi.StringField('state',
          searchable=1,
          languageIndependent=0,
          vocabulary='selection_state',
          widget=atapi.SelectionWidget(
             label=_(u'state'),

             ),
          ),

) + tuple(fields))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

kontratazioaSchema['title'].storage = atapi.AnnotationStorage()
kontratazioaSchema['description'].storage = atapi.AnnotationStorage()


kontratazioaSchema.changeSchemataForField('title', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('description', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('file_number', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('contract_type', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('process', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('izapidea', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('organization', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('kontratazio_organoa', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('published_date', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('published_date_boletin', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('organo_contratacion_date', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('last_date', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('eskaintza_ekonomikoa_date', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('kontratuasinatu_date', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('lizitazio_aurrekontua', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('documentation', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('attach1', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('attach1_information', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('attach2', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('attach3', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('attach4', 'lizitazioa')

kontratazioaSchema.changeSchemataForField('behin_behineko_file', 'adjudikazioa')
kontratazioaSchema.changeSchemataForField('behin_behineko_adjudikazio_date', 'adjudikazioa')
kontratazioaSchema.changeSchemataForField('behin_behineko_adjudikazioduna', 'adjudikazioa')
kontratazioaSchema.changeSchemataForField('behin_behineko_adjudikazioaren_zenbatekoa', 'adjudikazioa')
kontratazioaSchema.changeSchemataForField('behin_behineko_profile_date', 'adjudikazioa')

kontratazioaSchema.changeSchemataForField('behin_betiko_file', 'formalizazioa')
kontratazioaSchema.changeSchemataForField('behin_betiko_adjudikazio_date', 'formalizazioa')
kontratazioaSchema.changeSchemataForField('behin_betiko_adjudikazioduna', 'formalizazioa')
kontratazioaSchema.changeSchemataForField('behin_betiko_adjudikazioaren_zenbatekoa', 'formalizazioa')
kontratazioaSchema.changeSchemataForField('behin_betiko_profile_date', 'formalizazioa')
kontratazioaSchema.changeSchemataForField('state', 'egoera')

kontratazioaSchema.changeSchemataForField('language', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('relatedItems', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('allowDiscussion', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('subject', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('location', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('contributors', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('creators', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('effectiveDate', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('expirationDate', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('rights', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('creation_date', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('modification_date', 'lizitazioa')
kontratazioaSchema.changeSchemataForField('constrainTypesMode', 'lizitazioa')
kontratazioaSchema['language'].widget.visible['edit']='invisible'
kontratazioaSchema['relatedItems'].widget.visible['edit']='invisible'
kontratazioaSchema['allowDiscussion'].widget.visible['edit']='invisible'
kontratazioaSchema['subject'].widget.visible['edit']='invisible'
kontratazioaSchema['location'].widget.visible['edit']='invisible'
kontratazioaSchema['contributors'].widget.visible['edit']='invisible'
kontratazioaSchema['creators'].widget.visible['edit']='invisible'
kontratazioaSchema['effectiveDate'].widget.visible['edit']='invisible'
kontratazioaSchema['expirationDate'].widget.visible['edit']='invisible'
kontratazioaSchema['rights'].widget.visible['edit']='invisible'
kontratazioaSchema['creation_date'].widget.visible['edit']='invisible'
kontratazioaSchema['modification_date'].widget.visible['edit']='invisible'
kontratazioaSchema['constrainTypesMode'].widget.visible['edit']='invisible'

#schemata.finalizeATCTSchema(
#    kontratazioaSchema,
#    folderish=True,
#    moveDiscussion=False
#)

kontratazioaSchema.delSchemata('default')
kontratazioaSchema.delSchemata('categorization')
kontratazioaSchema.delSchemata('dates')
kontratazioaSchema.delSchemata('ownership')
#kontratazioaSchema.delSchemata('settings')


class kontratazioa(folder.ATFolder):

    implements(Ikontratazioa)

    meta_type = "kontratazioa"
    schema = kontratazioaSchema
    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    def selection_contract_type(self):
        return aq_parent(self).getContract_type()

    def selection_process(self):
        return aq_parent(self).getProcess()

    def selection_izapidea(self):
        return aq_parent(self).getIzapidea()

    def selection_organization(self):
        return aq_parent(self).getOrganization_source()

    def selection_kontratazio_organoa(self):
        return aq_parent(self).getKontratazio_organoa()

    def selection_state(self):
        return aq_parent(self).getState_source()

    def publication_year(self):
        if self.getPublished_date():
            return self.getPublished_date().year()
        else:
            return 1

    def behin_betiko_adjudikazio_date_function(self):
        if self.getBehin_betiko_adjudikazio_date():
            return self.getBehin_betiko_adjudikazio_date().year()
        else:
            return 1

    def kontratazioa_contract_type(self):
        return self.getContract_type()

atapi.registerType(kontratazioa, PROJECTNAME)

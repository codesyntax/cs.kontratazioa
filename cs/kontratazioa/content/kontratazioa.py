"""Definition of the kontratazioa content type
"""

from zope.interface import implements, directlyProvides
try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from Acquisition import aq_inner, aq_parent
from cs.kontratazioa import kontratazioaMessageFactory as _
from cs.kontratazioa.interfaces import Ikontratazioa
from cs.kontratazioa.config import PROJECTNAME

kontratazioaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

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
            description=_(u"Description of file_number"),
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
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"published_date"),
            description=_(u"Description of published_date"),
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name='published_date_boletin',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"published_date_boletin"),
            description=_(u"Description of published_date_boletin"),
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name='organo_contratacion_date',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"organo_contratacion_date"),
            description=_(u"Description of organo_contratacion_date"),
            show_hm=False,
        ),
    ),	 
    atapi.DateTimeField(
        name='last_date',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"last_date"),
            description=_(u"Description of last_date"),
        ),
    ),

    atapi.DateTimeField(
        name='eskaintza_ekonomikoa_date',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"eskaintza_ekonomikoa_date"),
            description=_(u"Description of eskaintza_ekonomikoa_date"),
        ),
    ),
    atapi.DateTimeField(
        name='kontratuasinatu_date',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"Kontratua sinatzeko data"),
            description=_(u"kontratua sinatzeko data"),
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
            description=_(u"Description of lizitazio_aurrekontua"),
        ),
    ),
    atapi.TextField('documentation',
                        required=False,
                        searchable=True,
			storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'put_documentation'),
                                                description=_(u'Description of documentation'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),
   
     atapi.FileField('attach1',
                  searchable=1,
		  languageIndependent=1,
                  storage = atapi.AnnotationStorage(migrate=True),
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
                                                description=_(u'Description of attach1_information'),
                                                rows=10,
                                                allow_file_upload=False),
                   ),
     atapi.FileField('attach2',
                  searchable=1,
                  storage = atapi.AnnotationStorage(migrate=True),
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
                  storage = atapi.AnnotationStorage(migrate=True),
		  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u'attach4'),
                     ),
                  ),

    
    atapi.FileField('behin_behineko_file',
                  searchable=1,
                  storage = atapi.AnnotationStorage(migrate=True),
		  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label=_(u'behin_behineko_file'),
                     ),
                  ),
    atapi.DateTimeField(
        name='behin_behineko_adjudikazio_date',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"behin_behineko_adjudikazio_date"),
            description=_(u"Description of behin_behineko_adjudikazio_date"),
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
                                                description=_(u'Description of behin_behineko_adjudikazioduna'),
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
                                                description=_(u'Description of behin_behineko_adjudikazioaren_zenbatekoa'),
                                                rows=10,
                                                allow_file_upload=False),
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
            description=_(u"Description of behin_behineko_profile_date"),
            show_hm=False,
        ),
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
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"behin_betiko_adjudikazio_date"),
            description=_(u"Description of behin_behineko_adjudikazio_date"),
            show_hm=False,
        ),
    ),
    atapi.TextField('behin_betiko_adjudikazioduna',
                        required=False,
                        searchable=True,
			storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'behin_betiko_adjudikazioduna'),
                                                description=_(u'Description of behin_betiko_adjudikazioduna'),
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
                                                description=_(u'Description of behin_betiko_adjudikazioaren_zenbatekoa'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),

    atapi.DateTimeField(
        name='behin_betiko_profile_date',
        storage = atapi.AnnotationStorage(),
        required=False,
        languageIndependent=1,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.CalendarWidget(
            label=_(u"behin_betiko_profile_date"),
            description=_(u"Description of behin_betiko_profile_date"),
        ),
    ),

    atapi.StringField('state',
                  searchable=1,
		  languageIndependent=0,
		  vocabulary='selection_state',
                  widget=atapi.SelectionWidget(
                     label=_(u'state'),
		     
                     ),
                  ),	 
    
))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

kontratazioaSchema['title'].storage = atapi.AnnotationStorage()
kontratazioaSchema['description'].storage = atapi.AnnotationStorage()
#kontratazioaSchema['behin_betiko_file'].widget.visible = {'edit':'hidden','view':'hidden'}
schemata.finalizeATCTSchema(
    kontratazioaSchema,
    folderish=True,
    moveDiscussion=False
)

class kontratazioa(folder.ATFolder):
    """Description of the Example Type"""
    implements(Ikontratazioa)

    meta_type = "kontratazioa"
    schema = kontratazioaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    def selection_contract_type(self):
            #import pdb;pdb.set_trace()
            situation_list=aq_parent(self).getContract_type()
            
            return situation_list
    def selection_process(self):
            #import pdb;pdb.set_trace()
            situation_list=aq_parent(self).getProcess()
            
            return situation_list
    def selection_izapidea(self):
            #import pdb;pdb.set_trace()
            situation_list=aq_parent(self).getIzapidea()
            
            return situation_list
    def selection_organization(self):
            #import pdb;pdb.set_trace()
            situation_list=aq_parent(self).getOrganization_source()
            
            return situation_list
    def selection_kontratazio_organoa(self):
            #import pdb;pdb.set_trace()
            situation_list=aq_parent(self).getKontratazio_organoa()
            
            return situation_list
    def selection_state(self):
            #import pdb;pdb.set_trace()
            situation_list=aq_parent(self).getState_source()
            
            return situation_list

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

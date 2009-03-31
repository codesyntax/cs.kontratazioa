"""Definition of the kontratazioa content type
"""

from zope.interface import implements, directlyProvides

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
		  vocabulary='selection_contract_type',
                  widget=atapi.SelectionWidget(
                     label='contract_type',
                     label_msgid='label_contract_type',
                     description_msgid='description_contract_type',
		     
                     ),
                  ),	 
    atapi.StringField('process',
                  searchable=1,
		  languageIndependent=0,
		  vocabulary='selection_process',
                  widget=atapi.SelectionWidget(
                     label='process',
                     label_msgid='label_process',
                     description_msgid='description_process',
		     
                     ),
                  ),	 
    atapi.StringField('izapidea',
                  searchable=1,
		  languageIndependent=0,
		  vocabulary='selection_izapidea',
                  widget=atapi.SelectionWidget(
                     label='izapidea',
                     label_msgid='label_izapidea',
                     description_msgid='description_izapidea',
		     
                     ),
                  ),	 
    atapi.StringField('organization',
                  searchable=1,
		  languageIndependent=0,
		  vocabulary='selection_organization',
                  widget=atapi.SelectionWidget(
                     label='organization',
                     label_msgid='label_organization',
                     description_msgid='description_organization',
		     
                     ),
                  ),	 
    atapi.StringField('kontratazio_organoa',
                  searchable=1,
		  languageIndependent=0,
		  vocabulary='selection_kontratazio_organoa',
                  widget=atapi.SelectionWidget(
                     label='izapidea',
                     label_msgid='label_kontratazio_organoa',
                     description_msgid='description_kontratazio_organoa',
		     
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
    atapi.StringField(
        name='lizitazio_aurrekontua',
        required=False,
        languageIndependent=1,
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
                        widget=atapi.RichWidget(label=_(u'documentation'),
                                                description=_(u'Description of documentation'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),
    atapi.TextField('information',
                        required=False,
                        searchable=True,
			storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'information'),
                                                description=_(u'Description of information'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),
     atapi.FileField('attach1',
                  searchable=1,
		  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label='attach1',
                     label_msgid='label_attach1',
                     description_msgid='description_attach1',
                     ),
                  ),
     atapi.FileField('attach2',
                  searchable=1,
		  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label='attach2',
                     label_msgid='label_attach2',
                     description_msgid='description_attach2',
                     ),
                  ),
     atapi.FileField('attach3',
                  searchable=1,
		  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label='attach3',
                     label_msgid='label_attach3',
                     description_msgid='description_attach3',
                     ),
                  ),
    atapi.StringField('state',
                  searchable=1,
		  languageIndependent=0,
		  vocabulary='selection_state',
                  widget=atapi.SelectionWidget(
                     label='state',
                     label_msgid='label_state',
                     description_msgid='description_state',
		     
                     ),
                  ),	 
    atapi.FileField('behin_behineko_file',
                  searchable=1,
		  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label='behin_behineko_file',
                     label_msgid='label_behin_behineko_file',
                     description_msgid='description_behin_behineko_file',
                     ),
                  ),
    atapi.TextField('behin_behineko_information',
                        required=False,
                        searchable=True,
			storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'behin_behineko_information'),
                                                description=_(u'Description of behin_behineko_information'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),
    atapi.FileField('behin_betiko_file',
                  searchable=1,
		  languageIndependent=1,
                  widget=atapi.FileWidget(
                     label='behin_betiko_file',
                     label_msgid='label_behin_betiko_file',
                     description_msgid='description_behin_betiko_file',
                     ),
                  ),
    atapi.TextField('behin_betiko_information',
                        required=False,
                        searchable=True,
			storage=atapi.AnnotationStorage(),
                        validators=('isTidyHtmlWithCleanup',),
                        default_output_type='text/x-html-safe',
                        widget=atapi.RichWidget(label=_(u'behin_betiko_information'),
                                                description=_(u'Description of behin_betiko_information'),
                                                rows=10,
                                                allow_file_upload=False),
                        ),
))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

kontratazioaSchema['title'].storage = atapi.AnnotationStorage()
kontratazioaSchema['description'].storage = atapi.AnnotationStorage()

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
            
atapi.registerType(kontratazioa, PROJECTNAME)

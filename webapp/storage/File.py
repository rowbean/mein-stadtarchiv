# encoding: utf-8

"""
Copyright (c) 2017, Ernesto Ruge
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import datetime
from flask import current_app
from mongoengine import Document, ReferenceField, DateTimeField, StringField, ListField, DecimalField, IntField, BooleanField, DictField
from .ArchivDocument import ArchivDocument

class File(Document, ArchivDocument):
    created = DateTimeField(default=datetime.datetime.now, datetime_format='datetime')
    modified = DateTimeField(default=datetime.datetime.now, datetime_format='datetime')
    binary_exists = BooleanField(default=False)
    name = StringField()
    fileName = StringField()
    text = StringField()

    sha1Checksum = StringField()
    mimeType = StringField()
    size = IntField()
    document = ReferenceField('Document', deref_document=False)

    externalId = StringField()

    pages = IntField()
    thumbnails = DictField(delete_document=True)
    thumbnailStatus = StringField(delete_document=True)
    thumbnailGenerated = DateTimeField(datetime_format='datetime', delete_document=True)

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<File %r>' % self.name

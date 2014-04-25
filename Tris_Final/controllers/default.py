    # -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import re

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

@auth.requires_login()
def search_uploads():
    q = request.get_vars['q']
    text = db(db.text1.email==auth.user.email).select(db.text1.ALL)
    voice = db(db.voice.email==auth.user.email).select(db.voice.ALL)
    out = []
    for i in text:
        tmp = re.findall(q, i['note'])
        if len(tmp) > 0 or i['tag'] == q or i['title'] == q:
            i['type'] = "text"
            out.append(i)
    for i in voice:
        tmp = re.findall(q, i['note'])
        if len(tmp) > 0 or i['tag'] == q or i['title'] == q:
            i['type'] = "voice"
            out.append(i)
    return dict(out=out)

@auth.requires_login()
def login_home():
    return dict()

def text():
    return dict()
@auth.requires_login()
def upload_file():
    form = SQLFORM(db.notes_upload)
    form.process()
    return dict(form = form)

@auth.requires_login()
def view():
    return dict()

@auth.requires_login()
def view_uploads():
    rows = db(db.notes_upload.email==auth.user.email).select(db.notes_upload.ALL)
    return dict(rows = rows)

@auth.requires_login()
def voice_uploads():
    rows = db(db.voice.email==auth.user.email).select(db.voice.ALL)
    return dict(rows = rows)
@auth.requires_login()
def text_uploads():
    rows = db(db.text1.email==auth.user.email).select(db.text1.ALL)
    return dict(rows = rows)

@auth.requires_login()
def temp():
    db.text1.insert(note=request.get_vars['note'], font=request.get_vars['font'], title=request.get_vars['title'], tag=request.get_vars['tag'])
    return dict()
    
@auth.requires_login()
def voice_upload():
    return dict()

@auth.requires_login()
def peak():
    if request.vars['type'] == 'text':
        rows = db(db.text1.email==auth.user.email).select(db.text1.ALL)
    elif request.vars['type'] == 'voice':
        rows = db(db.voice.email==auth.user.email).select(db.voice.ALL)       
    for row in rows:
        if request.vars['q'] == row.title:
            out = row
            break;
    return dict(out = out)

@auth.requires_login()
def voicedb():
    db.voice.insert(note=request.get_vars['text'],title=request.get_vars['head'], tag=request.get_vars['tag'])
    return dict()
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    request.vars._next=None
    auth.settings.register_next=URL(c='default',f='login_home')
    return dict(form=auth())

@auth.requires_login()
def edit():
    if request.vars['type'] == 'text':
        rows = db(db.text1.email==auth.user.email).select(db.text1.ALL)
    elif request.vars['type'] == 'voice':
        rows = db(db.voice.email==auth.user.email).select(db.voice.ALL)       
    for row in rows:
        if request.vars['q'] == row.title:
            out = row
            break;
    if request.vars['type'] != 'text':
        out['font'] = 'Arial'       
        out['type'] = 'voice'
    else:
        out['type'] = 'text'


    return dict(out = out)

@auth.requires_login()
def upd():
    if request.vars['type']=='text':
        rows = db(db.text1.email==auth.user.email).select(db.text1.ALL)
    elif request.vars['type']=='voice':
        rows = db(db.voice.email==auth.user.email).select(db.voice.ALL)
    for row in rows:
        if request.vars['title'] == row.title:
            out = row
            break;
    out.update_record(note=request.vars['note'])          
    return dict()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

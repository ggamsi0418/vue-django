def obj_to_post(obj):
    post = dict(vars(obj))

    if obj.modify_dt:
        # datetime을 string으로 변환
        post['modify_dt'] = obj.modify_dt.strftime('%Y-%m-%d %H:%M')
    else:
        post['modify_dt'] = ''

    if obj.owner_id:
        post['owner'] = {'id': obj.owner_id, 'username': obj.owner.username}
    else:
        post['owner'] = {'id': None, 'username': 'Anonymous'}

    if obj.tags:
        post['tags'] = [tag.name for tag in obj.tags.all()]
    else:
        post['tags'] = []

    # 필요없어서 삭제
    del post['_state']
    return post
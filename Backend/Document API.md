# DOCUMENT API

## Lấy danh sách các thể loại
    Url: api/categories/
    Method: GET
    Response status: HTTP 200 OK
    Response data: {
                     "id": int,
                     "name": string,
                     "description": string,
                     }

## Cập nhật mô tả của thể loại
    Url: api/categories/{category_id}/
    Method: PUT
    Response status: HTTP 200 OK
    Response data: {
                     "name": string,
                     "description": string,
                     }

## Lấy danh sách tất cả các bài báo, mỗi trang hiển thị 20 bài
    Url: api/articles/?page=?/
    Method: GET
    Response status: HTTP 200 OK
    Response data: {
                    "count": int,
                    "next": string,
                    "previous": string,
                    "results": [{
                        "id": int,
                        "category": string,
                        "author": string,
                        "title": string,
                        "description": string,
                        "content": string,
                        "date_posted": string,
                        "img": string,
                    }]
    }


## Truy cập chi tiết từng bài báo
    Url: api/articles/{article_id}/
    Method: GET
    Response status: HTTP 200 OK
    Response data: {
                    "count": int,
                    "next": string,
                    "previous": string,
                    "results": [{
                        "id": int,
                        "category": string,
                        "author": string,
                        "title": string,
                        "description": string,
                        "content": string,
                        "date_posted": string,
                        "img": string,
                    }]
    }

## Lấy danh sách bài báo của một thể loại
    Url: api/categories/{category_id}/articles/
    Method: GET
    Response status: HTTP 200 OK
    Response data: {
                    
                        "id": int,
                        "category": string,
                        "author": string,
                        "title": string,
                        "description": string,
                        "content": string,
                        "date_posted": string,
                        "img": string,
    }

## Tìm kiếm danh sách các bài báo theo từ khoá
    Url: api/articles/?q={key word}/
    Method: GET
    Response status: HTTP 200 OK
    Response data: {
                    "count": int,
                    "next": string,
                    "previous": string,
                    "results": [{
                        "id": int,
                        "category": string,
                        "author": string,
                        "title": string,
                        "description": string,
                        "content": string,
                        "date_posted": string,
                        "img": string,
                    }]
    }

## Tìm kiếm danh sách các bài báo theo từ khoá và theo thể loại
    Url: api/categories/{category_id}/articles/?q={key word}/
    Method: GET
    Response status: HTTP 200 OK
    Response data: {
                    "count": int,
                    "next": string,
                    "previous": string,
                    "results": [{
                        "id": int,
                        "category": string,
                        "author": string,
                        "title": string,
                        "description": string,
                        "content": string,
                        "date_posted": string,
                        "img": string,
                    }]
    }

## Đăng bài báo
    Url: api/articles/
    Method: POST
    Response status: HTTP 201 CREATED
    Content-Type: application/json
    Body = {
        "id": int,
        "category": int,
        "author": int,
        "title": string,
        "description": string,
        "content": string,
        "location": string,
        "img": string,

    }

## Active một bài báo
    Url: api/articles/{id}/active_article/
    Method: POST
    Response status: HTTP 200 OK
    Content-Type: application/json
    Body = {
        "id": int,
        "category": int,
        "author": int,
        "title": string,
        "description": string,
        "content": string,
        "date_posted": string,
        "img": string,
    }

## Ẩn một bài báo
    Url: api/articles/{id}/hide_article/
    Method: POST
    Response status: HTTP 200 OK
    Content-Type: application/json
    Body = {
        "id": int,
        "category": int,
        "author": int,
        "title": string,
        "description": string,
        "content": string,
        "date_posted": string,
        "img": string,
    }

## Xem danh sách các subscriber
    Url: api/subscribers/
    Method: GET
    Response status: HTTP 200 OK
    Response data = {
                        "count": int,
                        "next": string,
                        "previous": string,
                        "results": [{
                            ""id": int,
                            "subscriber": string,
                        }]
                    }

## Thêm subscriber vào danh sách
    Url: api/subscribers/
    Method: POST
    Response status: HTTP 200 OK
    Content-Type: application/json
    Body = {
        "subscriber": string
    }

## Truy cập chi tiết subscriber
    Url: api/subscribers/{id}
    Method: GET
    Response status: HTTP 200 OK
    Response data = {
                        
                        ""id": int,
                        "subscriber": string,
                        "categories": [
                            {
                                "name": string
                            },
                        ]
                    }

## Đăng kí thể loại cho subscriber
    Url: api/subscribers/1/add_category/
    Method: POST
    Response status: HTTP 200 OK
    Content-Type: application/json
    Body = {
        "categories": [string]
    }

## Xoá subscriber
    Url: api/articles/{id}/delete/
    Method: POST
    Response status: HTTP 200 OK
    Content-Type: application/json
    Body = {
        "subscriber": "",
        "categories": "",
    }

## Xoá thể loại subscriber đã đăng kí
    Url: api/articles/{id}/delete_category/
    Method: POST
    Response status: HTTP 200 OK
    Content-Type: application/json
    Body = {
        "subscriber": "",
        "categories": "",
    }
CREATE TYPE msg_type AS ENUM ('普通消息', '翻牌', '直播','礼物','回复','图片','视频');

create table star_message(
    id timestamp without time zone not null primary key ,
    message_type msg_type not null ,
    money smallint default 0,
    content text,
    user_id integer not null ,
    source_id text not null ,
    reply_to text
);

create table star_info(
    id integer not null primary key ,
    onwerName text not null ,
    roomId text not null
);

create table fans_msg(

)

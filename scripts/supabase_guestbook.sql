-- 방명록(guestbook) 기능용 Supabase 스키마
-- 실행 방법: Supabase 대시보드 → SQL Editor → 아래 내용 붙여넣고 Run
-- (anon key로는 실행 불가 — 반드시 대시보드에서 직접 실행)

create table public.messages (
  id bigint generated always as identity primary key,
  name text not null check (char_length(name) between 1 and 50),
  content text not null check (char_length(content) between 1 and 500),
  created_at timestamptz not null default now()
);

-- RLS(행 단위 보안) 활성화
alter table public.messages enable row level security;

-- 누구나 읽기 가능
create policy "messages_select_public"
on public.messages
for select
to anon, authenticated
using (true);

-- 누구나 작성 가능
create policy "messages_insert_public"
on public.messages
for insert
to anon, authenticated
with check (true);

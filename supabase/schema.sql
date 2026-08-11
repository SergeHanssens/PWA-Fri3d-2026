-- Fri3d gezinsplanner — gedeelde opslag voor de planningen.
-- Voer dit uit in de SQL Editor van je Supabase-project.

create table if not exists fri3d_plans (
  group_id text    not null,
  person   text    not null,
  label    text,                       -- weergavenaam, mag elders gewijzigd worden
  avatar   text,                       -- emoji; foto's blijven lokaal
  deleted  boolean not null default false,
  "add"    jsonb   not null default '[]',
  rm       jsonb   not null default '[]',
  ts       bigint  not null default 0,
  primary key (group_id, person)
);

-- Bestaande tabel uit een oudere versie bijwerken:
alter table fri3d_plans add column if not exists label   text;
alter table fri3d_plans add column if not exists avatar  text;
alter table fri3d_plans add column if not exists deleted boolean not null default false;

alter table fri3d_plans enable row level security;

-- De groepscode is het enige geheim. Kies er een die niet te raden is en
-- deel hem alleen via de uitnodigingslink.
drop policy if exists "gezin leest"    on fri3d_plans;
drop policy if exists "gezin schrijft" on fri3d_plans;
drop policy if exists "gezin wijzigt"  on fri3d_plans;
create policy "gezin leest"    on fri3d_plans for select using (true);
create policy "gezin schrijft" on fri3d_plans for insert with check (true);
create policy "gezin wijzigt"  on fri3d_plans for update using (true) with check (true);

notify pgrst, 'reload schema';

-- Opruimen na het kamp:
-- delete from fri3d_plans where group_id = 'jouwgroep-xxxxxx';

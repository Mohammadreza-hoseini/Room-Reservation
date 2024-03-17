CREATE TYPE "choose_rate" AS ENUM (
  'one',
  'two',
  'three',
  'four',
  'five'
);

CREATE TYPE "choose_day" AS ENUM (
  'saturday',
  'sunday',
  'monday',
  'tuesday',
  'wednesday',
  'thursday',
  'friday'
);

CREATE TABLE "newuser" (
  "id" uuid PRIMARY KEY,
  "avatar" text,
  "phone_number" varchar,
  "otp" integer,
  "otp_expire" datetime
);

CREATE TABLE "teamleader" (
  "id" uuid PRIMARY KEY,
  "leader" uuid
);

CREATE TABLE "teammembers" (
  "id" uuid PRIMARY KEY,
  "leader" uuid
);

CREATE TABLE "newuser_teammembers" (
  "user_id" uuid,
  "team_id" uuid
);

CREATE TABLE "comment" (
  "id" uuid PRIMARY KEY,
  "body" text,
  "author" uuid,
  "room" uuid,
  "status" bool DEFAULT false,
  "rate" choose_rate
);

CREATE TABLE "calendar" (
  "id" uuid PRIMARY KEY,
  "day" choose_day,
  "start_time" timestamp,
  "end_time" timestamp,
  "date" datetime,
  "is_active" bool DEFAULT true
);

CREATE TABLE "room" (
  "id" uuid PRIMARY KEY,
  "title" varchar,
  "created_at" datetime,
  "status" bool DEFAULT false,
  "capacity" integer DEFAULT 0
);

CREATE TABLE "calendar_room" (
  "room_id" uuid,
  "calendar_id" uuid
);

CREATE TABLE "reservation" (
  "id" uuid,
  "room_id" uuid,
  "leader" uuid,
  "created_at" datetime
);

ALTER TABLE "teamleader" ADD FOREIGN KEY ("leader") REFERENCES "newuser" ("id");

ALTER TABLE "teammembers" ADD FOREIGN KEY ("leader") REFERENCES "teamleader" ("leader");

ALTER TABLE "newuser_teammembers" ADD FOREIGN KEY ("user_id") REFERENCES "newuser" ("id");

ALTER TABLE "newuser_teammembers" ADD FOREIGN KEY ("team_id") REFERENCES "teammembers" ("id");

ALTER TABLE "comment" ADD FOREIGN KEY ("author") REFERENCES "newuser" ("id");

ALTER TABLE "comment" ADD FOREIGN KEY ("room") REFERENCES "room" ("id");

ALTER TABLE "calendar_room" ADD FOREIGN KEY ("room_id") REFERENCES "room" ("id");

ALTER TABLE "calendar_room" ADD FOREIGN KEY ("calendar_id") REFERENCES "calendar" ("id");

ALTER TABLE "reservation" ADD FOREIGN KEY ("room_id") REFERENCES "room" ("id");

ALTER TABLE "reservation" ADD FOREIGN KEY ("leader") REFERENCES "teamleader" ("id");

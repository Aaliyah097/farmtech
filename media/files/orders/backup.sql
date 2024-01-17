--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5 (Debian 15.5-1.pgdg120+1)
-- Dumped by pg_dump version 15.5 (Debian 15.5-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: address_versions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.address_versions (
    id uuid NOT NULL,
    user_id uuid NOT NULL,
    postal_code character varying(255) NOT NULL,
    house character varying(255) DEFAULT NULL::character varying,
    block character varying(255) DEFAULT NULL::character varying,
    building character varying(255) DEFAULT NULL::character varying,
    apartment character varying(255) DEFAULT NULL::character varying,
    region_type character varying(255) DEFAULT NULL::character varying,
    region_name character varying(255) DEFAULT NULL::character varying,
    district_type character varying(255) DEFAULT NULL::character varying,
    district_name character varying(255) DEFAULT NULL::character varying,
    settlement_type character varying(255) NOT NULL,
    settlement_name character varying(255) NOT NULL,
    micro_district_type character varying(255) DEFAULT NULL::character varying,
    micro_district_name character varying(255) DEFAULT NULL::character varying,
    street_type character varying(255) DEFAULT NULL::character varying,
    street_name character varying(255) DEFAULT NULL::character varying
);


ALTER TABLE public.address_versions OWNER TO postgres;

--
-- Name: COLUMN address_versions.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.address_versions.id IS '(DC2Type:ulid)';


--
-- Name: COLUMN address_versions.user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.address_versions.user_id IS '(DC2Type:ulid)';


--
-- Name: children; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.children (
    id uuid NOT NULL,
    surname character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    patronymic character varying(255) NOT NULL,
    gender character varying(255) NOT NULL,
    birth_date date NOT NULL
);


ALTER TABLE public.children OWNER TO postgres;

--
-- Name: COLUMN children.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.children.id IS '(DC2Type:ulid)';


--
-- Name: COLUMN children.birth_date; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.children.birth_date IS '(DC2Type:date_immutable)';


--
-- Name: contacts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contacts (
    id uuid NOT NULL,
    user_id uuid NOT NULL,
    email character varying(255) NOT NULL,
    phone character varying(255) NOT NULL
);


ALTER TABLE public.contacts OWNER TO postgres;

--
-- Name: COLUMN contacts.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.contacts.id IS '(DC2Type:ulid)';


--
-- Name: COLUMN contacts.user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.contacts.user_id IS '(DC2Type:ulid)';


--
-- Name: divisions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.divisions (
    id uuid NOT NULL,
    parent_id uuid,
    name character varying(255) NOT NULL
);


ALTER TABLE public.divisions OWNER TO postgres;

--
-- Name: COLUMN divisions.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.divisions.id IS '(DC2Type:ulid)';


--
-- Name: COLUMN divisions.parent_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.divisions.parent_id IS '(DC2Type:ulid)';


--
-- Name: finance_report_reasons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.finance_report_reasons (
    id uuid NOT NULL,
    name character varying(255) NOT NULL,
    type character varying(255) NOT NULL
);


ALTER TABLE public.finance_report_reasons OWNER TO postgres;

--
-- Name: COLUMN finance_report_reasons.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.finance_report_reasons.id IS '(DC2Type:ulid)';


--
-- Name: job_periods; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.job_periods (
    id uuid NOT NULL,
    user_id uuid NOT NULL,
    position_id uuid NOT NULL,
    division_id uuid NOT NULL,
    director_id uuid,
    start_date date NOT NULL,
    end_date date
);


ALTER TABLE public.job_periods OWNER TO postgres;

--
-- Name: COLUMN job_periods.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.job_periods.id IS '(DC2Type:ulid)';


--
-- Name: COLUMN job_periods.user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.job_periods.user_id IS '(DC2Type:ulid)';


--
-- Name: COLUMN job_periods.position_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.job_periods.position_id IS '(DC2Type:ulid)';


--
-- Name: COLUMN job_periods.division_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.job_periods.division_id IS '(DC2Type:ulid)';


--
-- Name: COLUMN job_periods.director_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.job_periods.director_id IS '(DC2Type:ulid)';


--
-- Name: COLUMN job_periods.start_date; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.job_periods.start_date IS '(DC2Type:date_immutable)';


--
-- Name: COLUMN job_periods.end_date; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.job_periods.end_date IS '(DC2Type:date_immutable)';


--
-- Name: passport_versions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.passport_versions (
    id uuid NOT NULL,
    user_id uuid NOT NULL,
    number character varying(255) NOT NULL,
    issue_date date NOT NULL,
    issued_by text NOT NULL,
    division_code character varying(255) NOT NULL,
    surname character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    patronymic character varying(255) NOT NULL,
    gender character varying(255) NOT NULL,
    birth_date date NOT NULL
);


ALTER TABLE public.passport_versions OWNER TO postgres;

--
-- Name: COLUMN passport_versions.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.passport_versions.id IS '(DC2Type:ulid)';


--
-- Name: COLUMN passport_versions.user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.passport_versions.user_id IS '(DC2Type:ulid)';


--
-- Name: COLUMN passport_versions.issue_date; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.passport_versions.issue_date IS '(DC2Type:date_immutable)';


--
-- Name: COLUMN passport_versions.birth_date; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.passport_versions.birth_date IS '(DC2Type:date_immutable)';


--
-- Name: positions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.positions (
    id uuid NOT NULL,
    name character varying(255) NOT NULL,
    director boolean NOT NULL
);


ALTER TABLE public.positions OWNER TO postgres;

--
-- Name: COLUMN positions.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.positions.id IS '(DC2Type:ulid)';


--
-- Name: responsibility_regions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.responsibility_regions (
    id uuid NOT NULL,
    parent_id uuid,
    name character varying(255) NOT NULL
);


ALTER TABLE public.responsibility_regions OWNER TO postgres;

--
-- Name: COLUMN responsibility_regions.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.responsibility_regions.id IS '(DC2Type:ulid)';


--
-- Name: COLUMN responsibility_regions.parent_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.responsibility_regions.parent_id IS '(DC2Type:ulid)';


--
-- Name: roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles (
    id character varying(255) NOT NULL
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- Name: roles_hierarchy; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles_hierarchy (
    role_id character varying(255) NOT NULL,
    child_role_id character varying(255) NOT NULL
);


ALTER TABLE public.roles_hierarchy OWNER TO postgres;

--
-- Name: user_job_periods_responsibility_regions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_job_periods_responsibility_regions (
    job_period_id uuid NOT NULL,
    responsibility_region_id uuid NOT NULL
);


ALTER TABLE public.user_job_periods_responsibility_regions OWNER TO postgres;

--
-- Name: COLUMN user_job_periods_responsibility_regions.job_period_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.user_job_periods_responsibility_regions.job_period_id IS '(DC2Type:ulid)';


--
-- Name: COLUMN user_job_periods_responsibility_regions.responsibility_region_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.user_job_periods_responsibility_regions.responsibility_region_id IS '(DC2Type:ulid)';


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id uuid NOT NULL,
    invited_by uuid,
    confirmed_by uuid,
    blocked boolean NOT NULL,
    on_confirmation boolean NOT NULL,
    login character varying(255) DEFAULT NULL::character varying,
    password_hash character varying(255) DEFAULT NULL::character varying,
    token_value character varying(255) DEFAULT NULL::character varying,
    token_expire timestamp(0) with time zone DEFAULT NULL::timestamp with time zone
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: COLUMN users.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users.id IS '(DC2Type:ulid)';


--
-- Name: COLUMN users.invited_by; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users.invited_by IS '(DC2Type:ulid)';


--
-- Name: COLUMN users.confirmed_by; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users.confirmed_by IS '(DC2Type:ulid)';


--
-- Name: COLUMN users.token_expire; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users.token_expire IS '(DC2Type:datetimetz_immutable)';


--
-- Name: users_children; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_children (
    user_id uuid NOT NULL,
    child_id uuid NOT NULL
);


ALTER TABLE public.users_children OWNER TO postgres;

--
-- Name: COLUMN users_children.user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users_children.user_id IS '(DC2Type:ulid)';


--
-- Name: COLUMN users_children.child_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users_children.child_id IS '(DC2Type:ulid)';


--
-- Name: users_roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_roles (
    role uuid NOT NULL,
    role_id character varying(255) NOT NULL
);


ALTER TABLE public.users_roles OWNER TO postgres;

--
-- Name: COLUMN users_roles.role; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.users_roles.role IS '(DC2Type:ulid)';


--
-- Data for Name: address_versions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.address_versions (id, user_id, postal_code, house, block, building, apartment, region_type, region_name, district_type, district_name, settlement_type, settlement_name, micro_district_type, micro_district_name, street_type, street_name) FROM stdin;
018c05ad-6c6d-0120-2143-fa2a52aa90b6	018c05aa-bbdc-796a-453b-728940661929	123456	\N	\N	\N	\N	\N	\N	\N	\N	город	Город	\N	\N	\N	\N
\.


--
-- Data for Name: children; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.children (id, surname, name, patronymic, gender, birth_date) FROM stdin;
\.


--
-- Data for Name: contacts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contacts (id, user_id, email, phone) FROM stdin;
018c05ab-97ce-a3b6-9a4f-af0cef40d0de	018c05aa-bbdc-796a-453b-728940661929	email@email.email	71112223344
\.


--
-- Data for Name: divisions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.divisions (id, parent_id, name) FROM stdin;
0187ce2e-cbfb-d4ef-0bbe-9718b883f3f7	\N	Pharmtec
\.


--
-- Data for Name: finance_report_reasons; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.finance_report_reasons (id, name, type) FROM stdin;
0153ce79-c49e-5772-67ef-8fc66a7f7a57	Фармкружок/Круглый стол	-
0153ce79-c49f-5bec-14e2-278940e55e7c	Авиабилеты, купленные в офисе	+
\.


--
-- Data for Name: job_periods; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.job_periods (id, user_id, position_id, division_id, director_id, start_date, end_date) FROM stdin;
018c05aa-bbdc-796a-453b-72894066192a	018c05aa-bbdc-796a-453b-728940661929	0153ce79-c490-034c-fc65-e01d81f21111	0187ce2e-cbfb-d4ef-0bbe-9718b883f3f7	\N	2023-11-25	\N
\.


--
-- Data for Name: passport_versions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.passport_versions (id, user_id, number, issue_date, issued_by, division_code, surname, name, patronymic, gender, birth_date) FROM stdin;
018c05ad-162e-3b70-b2f2-62e4c52196c6	018c05aa-bbdc-796a-453b-728940661929	1234567890	1985-01-01	-	123-456	Фамилия	Борис	Отчество	M	1985-01-01
\.


--
-- Data for Name: positions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.positions (id, name, director) FROM stdin;
0153ce79-c490-034c-fc65-e01d81f21111	Генеральный директор	t
\.


--
-- Data for Name: responsibility_regions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.responsibility_regions (id, parent_id, name) FROM stdin;
0153ce79-c481-9d78-5848-ecad811b2814	\N	Офис
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roles (id) FROM stdin;
ROLE_ADMIN
ROLE_FULL_RIGHTS
ROLE_OFFICE_MANAGER
ROLE_DIRECTOR
ROLE_ACCOUNTANT
\.


--
-- Data for Name: roles_hierarchy; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roles_hierarchy (role_id, child_role_id) FROM stdin;
\.


--
-- Data for Name: user_job_periods_responsibility_regions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_job_periods_responsibility_regions (job_period_id, responsibility_region_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, invited_by, confirmed_by, blocked, on_confirmation, login, password_hash, token_value, token_expire) FROM stdin;
018c05aa-bbdc-796a-453b-728940661929	018c05aa-bbdc-796a-453b-728940661929	018c05aa-bbdc-796a-453b-728940661929	f	f	boris	$2y$13$CXSV4LDtMiq4JreWg0h.huGhCC2nNu3UYlVBbMRnOdq8c/FZENcAu	244c40ef8248caf453e47f11771aa5a9	2023-12-14 12:42:32+03
\.


--
-- Data for Name: users_children; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_children (user_id, child_id) FROM stdin;
\.


--
-- Data for Name: users_roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_roles (role, role_id) FROM stdin;
018c05aa-bbdc-796a-453b-728940661929	ROLE_ADMIN
\.


--
-- Name: address_versions address_versions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.address_versions
    ADD CONSTRAINT address_versions_pkey PRIMARY KEY (id);


--
-- Name: children children_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.children
    ADD CONSTRAINT children_pkey PRIMARY KEY (id);


--
-- Name: contacts contacts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_pkey PRIMARY KEY (id);


--
-- Name: divisions divisions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.divisions
    ADD CONSTRAINT divisions_pkey PRIMARY KEY (id);


--
-- Name: finance_report_reasons finance_report_reasons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.finance_report_reasons
    ADD CONSTRAINT finance_report_reasons_pkey PRIMARY KEY (id);


--
-- Name: job_periods job_periods_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_periods
    ADD CONSTRAINT job_periods_pkey PRIMARY KEY (id);


--
-- Name: passport_versions passport_versions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passport_versions
    ADD CONSTRAINT passport_versions_pkey PRIMARY KEY (id);


--
-- Name: positions positions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.positions
    ADD CONSTRAINT positions_pkey PRIMARY KEY (id);


--
-- Name: responsibility_regions responsibility_regions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.responsibility_regions
    ADD CONSTRAINT responsibility_regions_pkey PRIMARY KEY (id);


--
-- Name: roles_hierarchy roles_hierarchy_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles_hierarchy
    ADD CONSTRAINT roles_hierarchy_pkey PRIMARY KEY (role_id, child_role_id);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- Name: user_job_periods_responsibility_regions user_job_periods_responsibility_regions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_job_periods_responsibility_regions
    ADD CONSTRAINT user_job_periods_responsibility_regions_pkey PRIMARY KEY (job_period_id, responsibility_region_id);


--
-- Name: users_children users_children_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_children
    ADD CONSTRAINT users_children_pkey PRIMARY KEY (user_id, child_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users_roles users_roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_roles
    ADD CONSTRAINT users_roles_pkey PRIMARY KEY (role, role_id);


--
-- Name: idx_1483a5e92dc9e5d6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_1483a5e92dc9e5d6 ON public.users USING btree (token_expire);


--
-- Name: idx_1483a5e9421ff255; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_1483a5e9421ff255 ON public.users USING btree (invited_by);


--
-- Name: idx_1483a5e9fb3f81cb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_1483a5e9fb3f81cb ON public.users USING btree (confirmed_by);


--
-- Name: idx_1c40c31727aca70; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_1c40c31727aca70 ON public.divisions USING btree (parent_id);


--
-- Name: idx_33401573a76ed395; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_33401573a76ed395 ON public.contacts USING btree (user_id);


--
-- Name: idx_51498a8e57698a6a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_51498a8e57698a6a ON public.users_roles USING btree (role);


--
-- Name: idx_51498a8ed60322ac; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_51498a8ed60322ac ON public.users_roles USING btree (role_id);


--
-- Name: idx_88dc48a7727aca70; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_88dc48a7727aca70 ON public.responsibility_regions USING btree (parent_id);


--
-- Name: idx_d39655a25e237e06; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_d39655a25e237e06 ON public.passport_versions USING btree (name);


--
-- Name: idx_d39655a296901f54; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_d39655a296901f54 ON public.passport_versions USING btree (number);


--
-- Name: idx_d39655a2a76ed395; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_d39655a2a76ed395 ON public.passport_versions USING btree (user_id);


--
-- Name: idx_d39655a2c7470a42; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_d39655a2c7470a42 ON public.passport_versions USING btree (gender);


--
-- Name: idx_d39655a2e42a05ab; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_d39655a2e42a05ab ON public.passport_versions USING btree (patronymic);


--
-- Name: idx_d39655a2e534d45a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_d39655a2e534d45a ON public.passport_versions USING btree (birth_date);


--
-- Name: idx_d39655a2e7769b0f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_d39655a2e7769b0f ON public.passport_versions USING btree (surname);


--
-- Name: idx_dad69a60a76ed395; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_dad69a60a76ed395 ON public.users_children USING btree (user_id);


--
-- Name: idx_dad69a60dd62c21b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_dad69a60dd62c21b ON public.users_children USING btree (child_id);


--
-- Name: idx_e3e31706b4b76ab7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_e3e31706b4b76ab7 ON public.roles_hierarchy USING btree (child_role_id);


--
-- Name: idx_e3e31706d60322ac; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_e3e31706d60322ac ON public.roles_hierarchy USING btree (role_id);


--
-- Name: idx_e753be53a76ed395; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_e753be53a76ed395 ON public.address_versions USING btree (user_id);


--
-- Name: idx_e7e378f2172fb384; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_e7e378f2172fb384 ON public.user_job_periods_responsibility_regions USING btree (responsibility_region_id);


--
-- Name: idx_e7e378f22b3b95cf; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_e7e378f22b3b95cf ON public.user_job_periods_responsibility_regions USING btree (job_period_id);


--
-- Name: idx_fdf82f3941859289; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_fdf82f3941859289 ON public.job_periods USING btree (division_id);


--
-- Name: idx_fdf82f39899fb366; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_fdf82f39899fb366 ON public.job_periods USING btree (director_id);


--
-- Name: idx_fdf82f39a76ed395; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_fdf82f39a76ed395 ON public.job_periods USING btree (user_id);


--
-- Name: idx_fdf82f39dd842e46; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_fdf82f39dd842e46 ON public.job_periods USING btree (position_id);


--
-- Name: uniq_1483a5e9aa08cb10; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX uniq_1483a5e9aa08cb10 ON public.users USING btree (login);


--
-- Name: uniq_1483a5e9bea95c75; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX uniq_1483a5e9bea95c75 ON public.users USING btree (token_value);


--
-- Name: uniq_1c40c315e237e06; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX uniq_1c40c315e237e06 ON public.divisions USING btree (name);


--
-- Name: uniq_d69fe57c5e237e06; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX uniq_d69fe57c5e237e06 ON public.positions USING btree (name);


--
-- Name: users fk_1483a5e9421ff255; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT fk_1483a5e9421ff255 FOREIGN KEY (invited_by) REFERENCES public.users(id);


--
-- Name: users fk_1483a5e9fb3f81cb; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT fk_1483a5e9fb3f81cb FOREIGN KEY (confirmed_by) REFERENCES public.users(id);


--
-- Name: divisions fk_1c40c31727aca70; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.divisions
    ADD CONSTRAINT fk_1c40c31727aca70 FOREIGN KEY (parent_id) REFERENCES public.divisions(id);


--
-- Name: contacts fk_33401573a76ed395; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT fk_33401573a76ed395 FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: users_roles fk_51498a8e57698a6a; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_roles
    ADD CONSTRAINT fk_51498a8e57698a6a FOREIGN KEY (role) REFERENCES public.users(id);


--
-- Name: users_roles fk_51498a8ed60322ac; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_roles
    ADD CONSTRAINT fk_51498a8ed60322ac FOREIGN KEY (role_id) REFERENCES public.roles(id) ON DELETE CASCADE;


--
-- Name: responsibility_regions fk_88dc48a7727aca70; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.responsibility_regions
    ADD CONSTRAINT fk_88dc48a7727aca70 FOREIGN KEY (parent_id) REFERENCES public.responsibility_regions(id) ON DELETE SET NULL;


--
-- Name: passport_versions fk_d39655a2a76ed395; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passport_versions
    ADD CONSTRAINT fk_d39655a2a76ed395 FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: users_children fk_dad69a60a76ed395; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_children
    ADD CONSTRAINT fk_dad69a60a76ed395 FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: users_children fk_dad69a60dd62c21b; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_children
    ADD CONSTRAINT fk_dad69a60dd62c21b FOREIGN KEY (child_id) REFERENCES public.children(id) ON DELETE CASCADE;


--
-- Name: roles_hierarchy fk_e3e31706b4b76ab7; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles_hierarchy
    ADD CONSTRAINT fk_e3e31706b4b76ab7 FOREIGN KEY (child_role_id) REFERENCES public.roles(id);


--
-- Name: roles_hierarchy fk_e3e31706d60322ac; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles_hierarchy
    ADD CONSTRAINT fk_e3e31706d60322ac FOREIGN KEY (role_id) REFERENCES public.roles(id);


--
-- Name: address_versions fk_e753be53a76ed395; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.address_versions
    ADD CONSTRAINT fk_e753be53a76ed395 FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: user_job_periods_responsibility_regions fk_e7e378f2172fb384; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_job_periods_responsibility_regions
    ADD CONSTRAINT fk_e7e378f2172fb384 FOREIGN KEY (responsibility_region_id) REFERENCES public.responsibility_regions(id) ON DELETE CASCADE;


--
-- Name: user_job_periods_responsibility_regions fk_e7e378f22b3b95cf; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_job_periods_responsibility_regions
    ADD CONSTRAINT fk_e7e378f22b3b95cf FOREIGN KEY (job_period_id) REFERENCES public.job_periods(id) ON DELETE CASCADE;


--
-- Name: job_periods fk_fdf82f3941859289; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_periods
    ADD CONSTRAINT fk_fdf82f3941859289 FOREIGN KEY (division_id) REFERENCES public.divisions(id);


--
-- Name: job_periods fk_fdf82f39899fb366; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_periods
    ADD CONSTRAINT fk_fdf82f39899fb366 FOREIGN KEY (director_id) REFERENCES public.job_periods(id) ON DELETE SET NULL;


--
-- Name: job_periods fk_fdf82f39a76ed395; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_periods
    ADD CONSTRAINT fk_fdf82f39a76ed395 FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: job_periods fk_fdf82f39dd842e46; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_periods
    ADD CONSTRAINT fk_fdf82f39dd842e46 FOREIGN KEY (position_id) REFERENCES public.positions(id);


--
-- PostgreSQL database dump complete
--


#!/usr/bin/env python3

"""
CONSTANTS
"""

from typing import Any
from pyutils import STATES, STATE_NAMES, STATE_FIPS


### PROJECT CONSTANTS ###

cycle: str = "2020"
yyyy: str = "2022"
yy: str = "22"
plan_type: str = "Congress"

study_states: list[str] = [
    "AL",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "FL",
    "GA",
    # "HI", # Hawaii BG's have contiguity issues that can't be corrected.
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "MA",
    "MD",
    # "ME", # Maine uses a mix of VTD's and BG's, which I can't easily handle.
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NH",
    "NV",
    "NJ",
    "NM",
    "NY",
    "NC",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "TN",
    "TX",
    "UT",
    "VA",
    "WA",
    "WI",
    "WV",
]  # 42 states with 2 or congressional districts (except HI and ME -- see above)

"""
States w/ only 1 congressional district not included:
AK 1
DE 1
ND 1
SD 1
VT 1
WY 1
"""

### ENVIRONMENT CONSTANTS ###

rawdata_dir: str = "../../../local/pg/rawdata"
vtd_dir: str = "../../../local/vtd_data/2020_vtd"

preprocessed_data_dir: str = "../../dev/baseline/data"

data_dir: str = "data"
temp_dir: str = "temp"

assets_dir: str = "docs/assets/images"
site_data_dir: str = "docs/_data"

dccvt_py: str = "../dccvt/examples/redistricting"
dccvt_go: str = "../dccvt/bin"


def unit_id(units: str) -> str:
    if units in ["block", "state"]:
        return "GEOID20"
    if units in ["bg", "tract"]:
        return "GEOID"
    raise ValueError(f"Invalid units: {units}")


### STATE META DATA ###

# State code helpers copied from dra2020/data_tools/ by way of pyutils

# Districts by state -- built from dra-types/lib/stateinfo.ts (11/04/2022)

districts_by_state: dict[str, Any] = {
    "AL": {"congress": 7, "upper": 35, "lower": 105},
    "AK": {"congress": 1, "upper": 20, "lower": 40},
    "AZ": {"congress": 9, "upper": 30, "lower": None},
    "AR": {"congress": 4, "upper": 35, "lower": 100},
    "CA": {"congress": 52, "upper": 40, "lower": 80},
    "CO": {"congress": 8, "upper": 35, "lower": 65},
    "CT": {"congress": 5, "upper": 36, "lower": 151},
    "DE": {"congress": 1, "upper": 21, "lower": 41},
    "FL": {"congress": 28, "upper": 40, "lower": 120},
    "GA": {"congress": 14, "upper": 56, "lower": 180},
    "HI": {"congress": 2, "upper": 25, "lower": 51},
    "ID": {"congress": 2, "upper": 35, "lower": None},
    "IL": {"congress": 17, "upper": 59, "lower": 118},
    "IN": {"congress": 9, "upper": 50, "lower": 100},
    "IA": {"congress": 4, "upper": 50, "lower": 100},
    "KS": {"congress": 4, "upper": 40, "lower": 125},
    "KY": {"congress": 6, "upper": 38, "lower": 100},
    "LA": {"congress": 6, "upper": 39, "lower": 105},
    "ME": {"congress": 2, "upper": 35, "lower": 151},
    "MD": {"congress": 8, "upper": 47, "lower": 67},
    "MA": {"congress": 9, "upper": 40, "lower": 160},
    "MI": {"congress": 13, "upper": 38, "lower": 110},
    "MN": {"congress": 8, "upper": 67, "lower": 134},
    "MS": {"congress": 4, "upper": 52, "lower": 122},
    "MO": {"congress": 8, "upper": 34, "lower": 163},
    "MT": {"congress": 2, "upper": 50, "lower": 100},
    "NE": {"congress": 3, "upper": 49, "lower": None},
    "NV": {"congress": 4, "upper": 21, "lower": 42},
    "NH": {"congress": 2, "upper": 24, "lower": 164},
    "NJ": {"congress": 12, "upper": 40, "lower": None},
    "NM": {"congress": 3, "upper": 42, "lower": 70},
    "NY": {"congress": 26, "upper": 63, "lower": 150},
    "NC": {"congress": 14, "upper": 50, "lower": 120},
    "ND": {"congress": 1, "upper": 47, "lower": 49},
    "OH": {"congress": 15, "upper": 33, "lower": 99},
    "OK": {"congress": 5, "upper": 48, "lower": 101},
    "OR": {"congress": 6, "upper": 30, "lower": 60},
    "PA": {"congress": 17, "upper": 50, "lower": 203},
    "RI": {"congress": 2, "upper": 38, "lower": 75},
    "SC": {"congress": 7, "upper": 46, "lower": 124},
    "SD": {"congress": 1, "upper": 35, "lower": 37},
    "TN": {"congress": 9, "upper": 33, "lower": 99},
    "TX": {"congress": 38, "upper": 31, "lower": 150},
    "UT": {"congress": 4, "upper": 29, "lower": 75},
    "VT": {"congress": 1, "upper": 13, "lower": 104},
    "VA": {"congress": 11, "upper": 40, "lower": 100},
    "WA": {"congress": 10, "upper": 49, "lower": None},
    "WV": {"congress": 2, "upper": 17, "lower": 100},
    "WI": {"congress": 8, "upper": 33, "lower": 99},
    "WY": {"congress": 1, "upper": 31, "lower": 62},
}


### OFFICIAL, NOTABLE, AND BASELINE MAPS ###

# Official congressional maps on 11/07/2022
# Pulled from data/state_plans.json copied the same day

official_maps: dict[str, str] = {
    "AL": "b1cfc3f6-27df-498d-a147-0664d75fea88",
    "AR": "fa3434ec-4f52-48de-947b-5998b6937bf0",
    "AZ": "4ee8ecf2-14b7-4a8d-99bc-82fa633a9305",
    "CA": "fc9d2d06-7c7f-451c-92cb-122127a79c29",
    "CO": "39f44408-23f7-439d-b7eb-923da58b63df",
    "CT": "707f203c-ce98-4de8-b150-a2605136e015",
    "FL": "3a6791b9-a186-4691-a95c-5d51dbb3be1c",
    "GA": "3a370cc7-f820-4af4-8fca-a27ec52502b7",
    "IA": "628d5e9a-bd35-4248-aa8c-73af095e0135",
    "IL": "8a4586ad-4c58-489b-828c-4477cfd0ce88",
    "IN": "c08c9df0-9756-4c5a-a7e7-01ff03bbb170",
    "KS": "2ea884cd-5687-48b4-879a-4f780d3de1cf",
    "KY": "0ec1616e-7ed6-4f84-b20d-dcc51221b2bf",
    "LA": "42873bd9-ce68-4ee1-878e-be420dbf0ee3",
    "MA": "791f8174-e00d-4baf-9b0a-206a298eb28b",
    "MD": "a365ecbd-db5f-4c84-a77f-90310c6a6c1a",
    "MI": "287ace43-1a66-4686-b596-949f578971a8",
    "MN": "4b212b88-2b8b-48aa-b2d2-e2f9980ac884",
    "MO": "68b2b598-69cd-430e-bee2-1dc4b76705f6",
    "MS": "2a63d0b3-58db-4e59-9b3b-436b221e078a",
    "NC": "6e8268a4-3b9b-4140-8f99-e3544a2f0816",
    "NE": "9de1188c-2169-4c5a-a4f3-76179d22b279",
    "NJ": "6ff0b024-2e5d-4e9b-ba0e-56f6de17ea80",
    "NM": "ec1c76cd-f59f-445b-8f24-fbffb0e8bdf5",
    "NV": "eb89e40d-595f-485f-9a43-d1bbdd6d0cb4",
    "NY": "395a7fbe-fa32-47fc-993d-e07d36baff72",
    "OH": "64d56870-70ea-4f4d-b667-9a4fd60ac511",
    "OK": "f726bcb3-b750-44b2-9d0b-e2df90fe6fa5",
    "OR": "9b2b545f-5cd2-4e0d-a9b9-cc3915a4750f",
    "PA": "b0a94d77-5d99-41c5-bc01-5859a6e1f3e6",
    "SC": "839561a1-8c15-4c4b-ab56-3275d68092f9",
    "TN": "445d4976-c994-473f-b14c-4b87464b07ee",
    "TX": "1c2c1e0d-2fd1-43a8-a039-73e7023124d1",
    "UT": "b4d46a7e-4366-4f6c-ac54-ff6640d4e13f",
    "VA": "bc930c25-236f-46a7-bbe9-d8d77e21d011",
    "WA": "3dd8f07d-8f9b-4905-a155-573bdc084b06",
    "WI": "aa64c8f5-837c-474f-819f-6eaa1094d776",
    # States w/ 2 congressional districts as of 07/16/23
    "ID": "ebc8cec8-b919-4a66-9b42-9cf5bf7e02a1",
    "MT": "66ff2b64-826d-48a9-bbe4-08afa4c10873",
    "NH": "a1a2b285-f862-402c-9e89-b45791a46473",
    "RI": "cffbb279-824c-47b8-90c7-3070378e37ae",
    "WV": "aaaa571f-f204-4cbe-bcf1-404db0519d36",
}

officials_copy: dict[str, str] = {
    "AL": "8c611540-7cb1-424c-b6b9-7ddc7f39abeb",
    "AR": "bba50394-d34c-4f0d-9056-8b9e6a029bfd",
    "AZ": "4a3d07fd-382c-441c-9c8d-af5d52987b87",
    "CA": "4daa293f-a347-4ba0-926e-3caebce864ea",
    "CO": "1d2c7749-d9bc-47b3-971f-e8025cc6d1da",
    "CT": "22a81014-0b6f-407d-acfa-99f464ed1039",
    "FL": "2e7debf0-c99b-4b54-9b99-df65d413d629",
    "GA": "e61aaae9-8af9-4339-8959-9c27f02e55d4",
    "IA": "ccbacbb9-dac8-4c48-b30b-42b0a6627e8f",
    "IL": "a5e1ee97-3727-4be1-80c7-8bfa7c72ee13",
    "IN": "da195dcd-381e-4598-bae4-9dad2ea12a8d",
    "KS": "cd94aec1-6e84-48d6-8922-5eea4f4c471f",
    "KY": "b38aeac3-297e-4ec4-9073-66215b9763c1",
    "LA": "a56db05b-6066-4cdc-89f3-e0b12ab7ea37",
    "MA": "8b9bdb2d-da5e-43db-acf1-08175c1718ba",
    "MD": "96d5e235-58de-4a46-a443-f5b6fabe0244",
    "MI": "55420ff6-a8a2-4291-afb3-6ec8c93e6872",
    "MN": "b382eee8-0eb8-4b5c-a9bb-7886972ed6b7",
    "MO": "57337b6a-45fc-4ee4-97a1-11540fd6c8a6",
    "MS": "7edecbd8-cdc5-4972-bcab-07bbd38259bb",
    "NC": "7b11a99a-6418-44cb-bc0e-ab5e040f6bae",
    "NE": "413dfcb2-0ec6-4459-9e3b-7cef2ddd8638",
    "NJ": "1f7c8393-0b8a-49ea-8fb4-60c393cfb661",
    "NM": "d2db917f-b700-4738-9a93-a38a43630c86",
    "NV": "c4077907-6605-4fd3-9493-50527ceee352",
    "NY": "11dc2c25-27a6-4259-b3dc-8e24fa21a086",
    "OH": "8290f680-abf8-4877-84a7-6075b31f9468",
    "OK": "bdd4c054-9a75-4117-9819-18673c1f9412",
    "OR": "9255d54b-36cc-4ca2-972d-fc330c975990",
    "PA": "bca4620c-bc4a-457e-a472-631ac20c3389",
    "SC": "68e91af2-1a68-4bc7-aa85-a48e52f07da3",
    "TN": "e142df57-8dd5-44c3-a316-c2675e0e2fe4",
    "TX": "89c7b67a-6164-42ee-89d4-072a4fca82c1",
    "UT": "a2845eee-af70-4c54-944f-08abd5b05471",
    "VA": "837303a3-ac0a-4fe3-b99e-b4e98f71d26a",
    "WA": "be06fce9-90a2-4bc0-9659-8eacafcd4afc",
    "WI": "130feb94-6532-4102-91de-92777af7c0d9",
    # States w/ 2 congressional districts: duplicated 07-16-23
    "ID": "ab09bc34-c83d-4327-9b59-c53c71682151",
    "MT": "d7fd9cdb-4677-47b0-930a-f53f6b044b8f",
    "NH": "8624cdac-7fd1-40ca-a47f-c196f8a84df7",
    "RI": "ee4cfa0f-930b-4f74-9adc-e3b4fc939a63",
    "WV": "8b2f8ec2-1d12-468a-b445-11c9f6097f74",
}  # Duplicated 11-16-22 (except for states w/ 2 congressional districts)

# Notable Maps for 42 states with 2 or congressional districts (except HI and ME -- see above)
# Pulled 11/07/2022 (except for states w/ 2 congressional districts)
notable_maps: dict[str, dict] = {
    "AL": {
        "proportional": "5d573512-b4c2-4f6f-ae2d-c922a10f44fb",
        "competitive": "3cd2a04e-cd87-40f5-a94f-6bdea8949c0d",
        "minority": "5d573512-b4c2-4f6f-ae2d-c922a10f44fb",
        "compact": "9a0a4eb9-8be2-4166-a58c-3df2847b9a52",
        "splitting": "9b7f6d4e-2afe-40c1-853f-4bbad07f9263",
    },
    "AZ": {
        "proportional": "13e2724a-cb3c-4751-92f6-c8f0476ea6bb",
        "competitive": "13e2724a-cb3c-4751-92f6-c8f0476ea6bb",
        "minority": "e5491bb3-b05d-449c-936d-0f3bdcadd2cd",
        "compact": "13e2724a-cb3c-4751-92f6-c8f0476ea6bb",
        "splitting": "11c9e5f4-b0bb-402a-aec9-f3104d80c443",
    },
    "AR": {
        "proportional": "22bd6016-ba50-4e4c-90bb-2711d589ba1f",
        "competitive": "719ae353-37dc-47ad-9c16-fc83451542a4",
        "minority": "20ee252a-a679-4a7d-8075-26f660699ab7",
        "compact": "fe847577-e642-48c7-9582-8eb23a959275",
        "splitting": "bf1ef1c3-56c9-4f31-9b07-0be1bbc1289e",
    },
    "CA": {
        "proportional": "04e6b230-5a5d-4e0c-b4f4-a49b331096a8",
        "competitive": "253d0168-5863-4991-856e-983c8676a1b5",
        "minority": "b79d4e43-2fc4-42cd-8370-de163c320368",
        "compact": "4bba5cca-2c5e-42d9-a49f-95f48e311f7c",
        "splitting": "774a680c-ad29-43d5-af16-6b9c6cc2f17f",
    },
    "CO": {
        "proportional": "8bdb3895-3b9a-4460-bbb9-c9888711a7c7",
        "competitive": "6f696afa-73e7-4ff4-8407-c4386d65ebd2",
        "minority": "28f40e7d-b056-4170-8337-ec92c596d572",
        "compact": "af01f470-753a-4247-862f-eeeb12604ec7",
        "splitting": "a78ca039-b9af-4816-ae03-6f842f3cab9c",
    },
    "CT": {
        "proportional": "7af97d6e-144a-4183-a83d-0dff2def50c2",
        "competitive": "7408228f-adfb-49b9-bf1a-28c754e7e413",
        "minority": "3d23b022-0589-404f-ab51-a75df5bd13e9",
        "compact": "9e314327-f2a7-4788-b415-1a55d0c3486e",
        "splitting": "e0cd942f-ee7f-40c0-a641-50ba23e08989",
    },
    "FL": {
        "proportional": "f9978e47-3746-4ae3-bc93-d634b3c0078c",
        "competitive": "77807f2e-5fbc-4b4c-93f4-078be63ab5ec",
        "minority": "01131b32-fe72-4572-aaef-696387136286",
        "compact": "f9978e47-3746-4ae3-bc93-d634b3c0078c",
        "splitting": "67d684eb-bcc9-4ca3-935d-ea7b77fdc8ba",
    },
    "GA": {
        "proportional": "4a96b0c9-ad11-4b64-aed1-314c09310438",
        "competitive": "db0689d4-7a77-4df5-a335-a57af2ed1da7",
        "minority": "682301e4-14b1-486a-a6b0-feac1c07670e",
        "compact": "a95a3daf-8eec-46ac-8454-c9b829e325c7",
        "splitting": "4a96b0c9-ad11-4b64-aed1-314c09310438",
    },
    "IL": {
        "proportional": "cbad09de-f1de-49da-95ff-1a6553d3d0e3",
        "competitive": "94f6e3fe-3f21-44eb-9321-dc2523a88ac3",
        "minority": "26977538-7b78-4dbf-95e0-28afc3ea7803",
        "compact": "cbb62424-78af-4dd8-811c-b9563ad59189",
        "splitting": "5fa6ed67-07a4-411a-a8a5-42920f367d84",
    },
    "IN": {
        "proportional": "6818af19-93ab-4f84-b25e-5248f6dccab6",
        "competitive": "e4c89f1e-3255-41a1-8e5d-0b587a8d2f52",
        "minority": "8bab38bd-cacb-4c6f-8dd2-21d359053176",
        "compact": "b80fc5ee-4642-4bd0-b60c-a3f0c485d765",
        "splitting": "b10f29da-ce52-4d2b-8c2e-39def8204419",
    },
    "IA": {
        "proportional": "237a6d9a-67b6-40c5-8b93-bbf0f39b53f9",
        "competitive": "49beb7b3-4328-45b0-ba46-1336e085180a",
        "minority": "d8b1efb6-089b-4059-bbd7-44d6cb4ad3e0",
        "compact": "848416dd-0b95-43e7-b6e5-47e896dd7565",
        "splitting": "2fd0aa0c-91fa-4239-8faf-936e300ab19e",
    },
    "KS": {
        "proportional": "cb7003a3-fc41-48db-b9cc-6c0c5afdb018",
        "competitive": "58741a3c-7777-4a4d-82bd-5d8252f37ae6",
        "minority": "b031e66b-4fd6-4b36-901a-5f857468fc6a",
        "compact": "df9a2ac9-be16-4380-9815-ae6a4ed4773a",
        "splitting": "b8e49933-96d2-4c80-a5f2-33e804a1ab57",
    },
    "KY": {
        "proportional": "4f0b4319-f1aa-4e8e-b55c-3100719974ec",
        "competitive": "2086785f-93e8-4268-9c7d-e3b60ddbf666",
        "minority": "eb314eae-f4e6-4b50-ba5e-5d77174dc0ec",
        "compact": "3a541d7a-192a-451d-a8bf-e01687292adb",
        "splitting": "ed7c4e05-3c95-4e89-b844-8a0f231ff195",
    },
    "LA": {
        "proportional": "312c0078-4688-4421-a6c7-c9751ded611f",
        "competitive": "48d5f83f-c070-4783-9893-d8bf889f095e",
        "minority": "312c0078-4688-4421-a6c7-c9751ded611f",
        "compact": "d3a27a1b-82f9-4749-ab09-7a2d1b563f02",
        "splitting": "1183a889-beae-45dd-81bf-96ffd1256ce2",
    },
    "MD": {
        "proportional": "e3e93c31-764c-4ce3-9bdc-6ee3c945df9a",
        "competitive": "e3e93c31-764c-4ce3-9bdc-6ee3c945df9a",
        "minority": "d8dc1ebe-058c-403a-926a-e5bd560369b4",
        "compact": "2a9b5438-2740-4980-918e-099050b3df94",
        "splitting": "70801f37-715e-4e7c-b203-c7789c244d4c",
    },
    "MA": {
        "proportional": "20f6aa40-ceb3-42a2-9d03-a6139efa3471",
        "competitive": "2bdbac0c-b6bc-4183-b160-52f019046447",
        "minority": "1dbadcc4-a0c2-42b0-863d-d5b54a44ced8",
        "compact": "af6430dc-008a-4d39-ad0a-c84bb2ffaa79",
        "splitting": "fffc7551-b217-43b3-86aa-0875c76f4549",
    },
    "MI": {
        "proportional": "517c0e1c-0e6d-4dc5-900c-8e15d6a65d23",
        "competitive": "63d3e83b-7e54-4e4d-81b0-9d2160c9a1dd",
        "minority": "c4cf8435-4c0f-4b59-b8ec-f74e593301a3",
        "compact": "19e6a5c0-25d7-4780-a95f-585ef0fb21cf",
        "splitting": "20a791e1-051c-4a25-a7a2-c38278c8dc71",
    },
    "MN": {
        "proportional": "a5322380-f9a1-40e7-a541-8f5ae2b5973f",
        "competitive": "190e7e43-3bb3-4373-93bd-defb9a1a783d",
        "minority": "e87547ac-3fe1-4dd5-8249-2736ab4616b7",
        "compact": "b66771be-1286-4b2c-928d-01337995c336",
        "splitting": "c168bd72-3e9f-4aa9-accb-703055567490",
    },
    "MS": {
        "proportional": "30887944-655c-4acc-a2e9-1e0c4b78137c",
        "competitive": "3aee6676-fb1f-45a2-a27d-11efa8072d48",
        "minority": "f2c96cf7-9c23-449e-81c2-72b8aaf388f3",
        "compact": "4fc7f506-0993-47ea-8459-37f89d326c25",
        "splitting": "592e3a73-cac8-4f00-a507-e339b44ad092",
    },
    "MO": {
        "proportional": "5f18a76c-f3ad-4ba1-8d50-1db6cec56f1f",
        "competitive": "5830b5c8-fb14-4af5-8acc-ec3dd27f448c",
        "minority": "d393f212-17c6-4de0-bf03-8afd288c5234",
        "compact": "35607bfd-2363-421b-8a0e-ec8252bcc4f0",
        "splitting": "189d6bd7-27fc-46bb-b4a7-93dc96dad09f",
    },
    "NE": {
        "proportional": "fad7dd6a-b3fb-44a2-b159-6634efd1a4b6",
        "competitive": "f9e38118-22d8-4493-a12d-509b7711324a",
        "minority": "d1f97366-8fb9-489a-a11c-a0b1ac10673b",
        "compact": "d1f97366-8fb9-489a-a11c-a0b1ac10673b",
        "splitting": "e3f66393-18fc-4d37-9599-32411ad2bf20",
    },
    "NV": {
        "proportional": "628a65f3-abf3-412b-9ef6-7cd20bfeac73",
        "competitive": "ad048a79-af54-4092-aa8f-f14a0947df4d",
        "minority": "cd1c643b-7353-4d8e-b9ab-072ef603508d",  # replaced
        "compact": "628a65f3-abf3-412b-9ef6-7cd20bfeac73",
        "splitting": "7b4f4269-1c31-4fa8-a282-cd8f1fa3b5e6",
    },
    "NJ": {
        "proportional": "be03805c-45c0-4bbd-8760-dc738705bcde",
        "competitive": "535e013f-5db5-4a9c-9edc-496d65972781",
        "minority": "1f2e6cb7-61aa-4a8b-8800-38ce8a767248",
        "compact": "6fcb6b8b-2565-4831-990f-b978b88cc253",
        "splitting": "c24cf3a7-541a-472a-9e3f-6ebe398e8c33",
    },
    "NM": {
        "proportional": "b3946cfb-7567-46a1-9fc5-6a226db7728d",
        "competitive": "b3946cfb-7567-46a1-9fc5-6a226db7728d",
        "minority": "b3946cfb-7567-46a1-9fc5-6a226db7728d",
        "compact": "714b1ebf-9280-463a-b02e-e1781196dd3a",
        "splitting": "3cab7943-cc5d-4c56-a460-307ca987324a",
    },
    "NY": {
        "proportional": "4185458d-6708-42ad-902c-ae9f9eb832bc",
        "competitive": "e8fcc5ee-9151-4ef8-9ef5-66fb80be9317",
        "minority": "fe733d47-6219-48ad-9a61-3a3933da7e61",
        "compact": "59761137-e122-48ff-980f-9538074360c8",
        "splitting": "72b69a87-0f16-4963-95a8-9d210bf14fb5",
    },
    "NC": {
        "proportional": "7cfcec86-b8bf-41fa-a6c2-0be9b3799747",
        "competitive": "40178c75-312d-4789-a457-d609b0d8a043",
        "minority": "3b168396-6666-4167-830e-4500bde459fe",
        "compact": "3bacb15d-e014-4764-9e8c-f238eb687d50",
        "splitting": "82e6303c-e842-469b-b364-918bcacf9ef3",
    },
    "OH": {
        "proportional": "c609d0a3-d838-4d92-b40b-f706a3e616f4",
        "competitive": "eb5ada10-d1d7-43c5-b02a-4c969bc5e5a2",
        "minority": "72489412-c5ba-4d8a-8f77-dad9e9a596f4",
        "compact": "c609d0a3-d838-4d92-b40b-f706a3e616f4",
        "splitting": "e8c64e09-f406-47a2-921b-eb08c1020803",
    },
    "OK": {
        "proportional": "8571df5b-1648-4465-8d00-5e0b36cd75c0",
        "competitive": "8d4d5241-fc6f-4c7d-b953-f5f7e0071e6d",
        "minority": "c42edda8-9784-4c3e-ad11-ba3512ee0845",
        "compact": "5d052539-7560-4200-9e96-c920cda86b4f",
        "splitting": "3dbef3e8-e5ff-4d81-8d81-cb4c55892461",
    },
    "OR": {
        "proportional": "409bed65-c9a0-452e-8b68-1f4f0b1dc67e",
        "competitive": "c73a3d8b-3648-4488-a6ce-cfd512f2c6b6",
        "minority": "bedb8c6a-5661-4cfc-ae59-6e51dd9d63d4",
        "compact": "b9215af6-e56d-4bd7-a414-75086e0e96eb",
        "splitting": "3eaf150c-fc28-4d24-b15e-606a5253e9d4",
    },
    "PA": {
        "proportional": "b1f9190b-4c0b-4c9d-a8f9-64d296c040fe",
        "competitive": "d88bcad5-2aea-462f-af79-269a0c85db19",
        "minority": "7e00b136-2831-42d4-a455-060a94e0af77",
        "compact": "8a2a7dac-1c36-47d4-91fb-3147fcb5e6dd",
        "splitting": "da43a46c-1ca4-41ab-acd2-e07ceff538fd",
    },
    "SC": {
        "proportional": "56fc8132-911f-4dc8-a624-405e65ed33af",
        "competitive": "3cd7600e-7a08-47b5-8175-252b70ce38ea",
        "minority": "71866f45-008e-4891-9a8b-b24763205725",
        "compact": "cb454bbb-950b-41c9-8d9e-0cba47e0c6ea",
        "splitting": "14fb2ae8-9e79-45d9-8492-30c07511a107",
    },
    "TN": {
        "proportional": "bb2bde21-934e-484b-90b5-496eb9bfbd44",
        "competitive": "a8d8ab31-92a8-4b7c-871e-91241c235b9e",
        "minority": "47a81f0b-4bc0-4069-a9f4-cd3c948a6ebd",
        "compact": "993cde69-8adf-4fef-8b90-475f8d525810",
        "splitting": "a94ff5a0-9d8a-4234-8a02-7ae698a2741a",
    },
    "TX": {
        "proportional": "9b000c6e-f8f5-4d50-b060-81f9c8ec8d21",
        "competitive": "ac91c9a3-331d-4b23-b2f5-8d5ca11e8e25",
        "minority": "a2120eda-e2ff-47d0-a06d-d8305eedd227",
        "compact": "ea165cec-8fd7-4c1e-854f-ecc789416873",
        "splitting": "a89fe1b1-7a37-4654-91bf-f6ac2c8fe661",
    },
    "UT": {
        "proportional": "5c881c02-483b-4df8-bfd1-c32486e31138",
        "competitive": "8c187e06-a4f8-4778-9ccc-d237ffc6f091",
        "minority": "1593ee86-9176-4e92-96b5-6f801f3e13e4",
        "compact": "5c881c02-483b-4df8-bfd1-c32486e31138",
        "splitting": "5c881c02-483b-4df8-bfd1-c32486e31138",
    },
    "VA": {
        "proportional": "31607948-2ad0-4e68-a8ce-e175fcfc3ddf",
        "competitive": "22700e82-9423-4029-b94a-78ebb16dc962",
        "minority": "479fcea5-a312-47bb-ba2d-377f3cbd1ea9",
        "compact": "55426dbf-1d87-45ce-b164-77d8ae985898",
        "splitting": "a0402468-c3cd-4858-b72d-a37eecb4ca16",
    },
    "WA": {
        "proportional": "7e3df196-530d-474d-85d2-12db2b865609",
        "competitive": "d544f633-89a5-4b8e-9080-d693bd527475",
        "minority": "7b82c987-3779-49c3-b1b8-df838580c9aa",
        "compact": "cab3e806-3015-4e65-8daa-d5267f949046",
        "splitting": "780082a2-bd41-4787-b18f-bfaf31fe8739",
    },
    "WI": {
        "proportional": "2b2705c6-7532-40eb-8521-af8bdc66de25",
        "competitive": "2786ff99-aead-4585-9246-ce2dbc5bcc47",
        "minority": "1943dc12-a393-4b9f-a688-cd5365e208f4",
        "compact": "b6942ec8-9615-4e6a-bdbd-275b196a840f",
        "splitting": "bc908f90-e0ad-4e92-8514-512cebebb637",
    },
    # States w/ 2 congressional districts
    "ID": {
        "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
        "competitive": "5f1c3e67-1895-4230-80c6-e7d286b6e89e",  # 07-16-23 replaced
        "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
        "compact": "206912f7-878a-4f21-b188-f40320ab558d",  # 07-16-23
        "splitting": "abd274f0-847c-4c53-934e-646c84d81aac",  # 07-16-23
    },
    "MT": {
        "proportional": "0c96f1a2-d4c9-4294-b2d4-a20aa9d2b04d",  # 07-16-23
        "competitive": "e1058b7d-1cca-46a0-98ec-d95dd3d353a1",  # 07-16-23
        "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
        "compact": "7838e111-d287-43c5-97ac-d04366cb6d1c",  # 07-16-23
        "splitting": "a50422e4-5596-4385-808b-7bf0639b5d63",  # 07-16-23
    },
    "NH": {
        "proportional": "7b509654-2390-440b-a022-211cb977b074",  # 07-16-23 replaced
        "competitive": "adce2bd3-8f35-4437-9dd5-86bb5e1864b1",  # 07-16-23
        "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
        "compact": "3ed6cd29-1807-4a82-a4e8-c6512d28ab77",  # 07-16-23
        "splitting": "adce2bd3-8f35-4437-9dd5-86bb5e1864b1",  # 07-16-23 replaced
    },
    "RI": {
        "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
        "competitive": "40aef9df-2406-4c9b-8e80-b48b273dfd32",  # 07-16-23 replaced
        "minority": "ffddb68e-700a-4d85-85f5-edfe061ec821",  # 07-16-23
        "compact": "344ecc9b-b641-44e7-87b2-1ffd6d69da87",  # 07-16-23
        "splitting": "344ecc9b-b641-44e7-87b2-1ffd6d69da87",  # 07-16-23
    },
    "WV": {
        "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
        "competitive": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
        "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
        "compact": "b497117a-9d00-471e-9d1a-b69ae960c48d",  # 07-16-23
        "splitting": "5e630f86-6a48-4942-b613-51d4c572af93",  # 07-16-23
    },
}

notables_copy: dict[str, dict] = {
    "AL": {
        "proportional": "e9851c4d-2b32-4da0-adaf-86762af78e26",
        "competitive": "9f3cd446-144f-4824-9ce2-3f6d52ebf74c",
        "minority": "14942ba2-c86f-4e7b-a1e7-51d7f243dd84",
        "compact": "b556aea8-e259-40e1-9b29-4e7572d6cbae",
        "splitting": "94c7b2b9-f8d0-4d89-aae1-53cfd9009f97",
    },
    "AZ": {
        "proportional": "318578e0-ae95-4319-aa7a-34838c016cdd",
        "competitive": "17345788-c122-43be-a62a-5c43a696a22c",
        "minority": "5b4dfad5-ee34-469d-bdef-7f07a749b2c5",
        "compact": "970224ba-4373-48fd-9e3e-15527b63c9c5",
        "splitting": "7ff7eec5-1b01-422b-bb34-d78da0f8fcb8",  # copy of "2dff53e3-4c0a-499b-b3c9-26e409318e83"
        # "splitting": "01aecc9a-2a4b-4d43-9ca7-96385c0d1daa",
    },
    "AR": {
        "proportional": "4331cceb-5317-4921-a620-1197799add51",
        "competitive": "9ff90f72-33bb-4d70-a7d6-91fb30502bf8",
        "minority": "d6e55da9-dd51-4429-ba40-78bbfe3105e4",
        "compact": "c53002fd-1f4e-4f3f-86c8-00e738d7cbe5",
        "splitting": "ea810d0f-a507-416e-a0f6-58adbf93df6e",
    },
    "CA": {
        "proportional": "e2b59dd7-629e-4856-9f35-b37751ee101e",
        "competitive": "ade2f538-fe9b-4e37-9a7e-d9c87ea717d5",
        "minority": "07cd471f-0ebc-449e-ad7f-534ec8d9e78d",
        "compact": "42bf9029-6e68-481a-be75-a1f339248cba",
        "splitting": "fbefc34b-ac86-4081-8731-b731d95e67f9",
    },
    "CO": {
        "proportional": "69886296-e646-4bb8-841f-40faf888463e",
        "competitive": "d11c4b86-1f01-4adb-8b70-7d17d640de46",
        "minority": "2427fc2b-4907-4fac-a1fd-54fe225db227",
        "compact": "e9e9c486-bb80-4ce5-9666-4466947f7ab0",  # copy of "7d34443b-3e8c-4108-9074-2e565805b89d"
        # "compact": "5970deaa-8306-4728-8933-3a74d1f2f298",
        "splitting": "d639dbaf-cf30-4998-b794-7cfba3312a0b",  # copy of "fe586498-24d8-4c7c-a6db-8437ed0b9ca6"
        # "splitting": "896e564c-ddfa-4596-9c3d-a6dbd9b6e886",
    },
    "CT": {
        "proportional": "6411d3ac-8523-44b2-a9e1-4abc0469790c",
        "competitive": "b10fcc44-6db9-435f-bd37-f1b8524e32b2",
        "minority": "2ce70cfc-ab32-48eb-a485-7d33bd201ff0",
        "compact": "d8e5dbfd-c7b1-48a9-a3ee-c606867acfe7",
        "splitting": "76865f59-03ed-4647-95a2-c6d64a7b9270",
    },
    "FL": {
        "proportional": "6ba89c54-906b-4753-85d1-c82caff8a597",
        "competitive": "19f48062-920f-4659-bcad-9b7b10b7a150",
        "minority": "9191dc5d-fef4-4920-825d-c1b29f842dc7",
        "compact": "35789bfa-b77d-4a42-a86d-5ce161d24514",
        "splitting": "94248293-2880-49b1-9dc3-cb8ff77f3e58",
    },
    "GA": {
        "proportional": "0f6d64be-4cdc-457e-8712-90514e74de9b",
        "competitive": "d83f0a86-bea5-4728-869b-207072f53bb3",
        "minority": "f3527d3c-41b5-4758-8560-6ba52695c3b8",
        "compact": "daec754f-45d0-43d3-bdbf-e8637e7cfe8d",
        "splitting": "bf30be3a-0924-4790-a353-83ca0152504a",
    },
    "IL": {
        "proportional": "0764d8de-7366-4572-8617-cdf5f00bbcbc",
        "competitive": "6e6ecb9a-2385-4b40-a0ce-b2217ce92c47",
        "minority": "0d4b32d4-bf9d-41a1-b15e-807daf0cc128",
        "compact": "6ff3964a-0009-4cc0-a643-0f8f9b2096b8",
        "splitting": "0cfac142-a509-447c-95a7-77c3b87d467d",
    },
    "IN": {
        "proportional": "1f6ff4fa-53ed-499a-81e7-cd80296c6946",
        "competitive": "32ee9012-f4d6-4425-9f88-b38c6ae4a70c",
        "minority": "101f80a9-cfc0-423b-b0d6-29e81403b46c",
        "compact": "f59e9631-2abe-4753-bc3a-b9a5186d233c",
        "splitting": "07f032b2-ec89-4bde-8ec5-57224285172c",
    },
    "IA": {
        "proportional": "b8cff1b2-059a-421c-92f1-168eecb0860d",
        "competitive": "a62a4544-8ab9-4641-849c-ab9f68e842bc",
        "minority": "d6e9ebe5-9e71-4e1d-adad-584868220635",
        "compact": "3888d170-52fe-44fb-8428-d0e08b8cdcf5",
        "splitting": "311d779b-9cfc-4983-a589-a9d6877e3f1e",
    },
    "KS": {
        "proportional": "177278c7-822b-414c-a6e4-47c49e6d8e31",  # copy of "5e0fe356-4f7f-49eb-b36b-693b1a156845"
        # "proportional": "659e9adf-713c-4375-9528-f384d043f1b0",
        "competitive": "cadda27c-9616-45b6-a872-2d5a6e60c6a1",  # copy of dfabfef9-429c-4b81-a893-da79e7e26214
        # "competitive": "e2021c4b-281c-451a-ad9e-49fef9c2f57b",
        "minority": "5e4b3a7d-cb16-4cee-ac4b-05086203c64d",
        "compact": "d86bf787-674a-4a6e-8cb8-e84c45762077",
        "splitting": "7ac2a17a-c287-41ff-b624-67efe0bea826",
    },
    "KY": {
        "proportional": "da1a0bdd-7f3d-43e4-892e-b1c111b46d4d",
        "competitive": "5c8fe427-5ca5-4168-a225-7c510aa85ef1",
        "minority": "036aeb13-a3c3-4ef6-8be8-5af7bab6b730",
        "compact": "424d91c3-a26e-4083-8790-06f8384d2c44",
        "splitting": "37c63cb2-3bec-418f-8fee-c841ddc5e3c1",
    },
    "LA": {
        "proportional": "38b5cae0-cc85-4eb7-aa0a-ff1cfd3db549",
        "competitive": "cc002cfc-68a1-4884-9cf1-f9a33c9b1add",
        "minority": "0be18b01-7044-4055-8de8-596a2cae3039",
        "compact": "fcc9a519-3aaa-4003-84cf-9807ec8bad4a",
        "splitting": "02689947-7712-4139-aa39-2e5ea6add817",
    },
    "MD": {
        "proportional": "55459ef3-26a1-421a-9267-d7a113c306dc",
        "competitive": "f98eba6b-5297-47d1-bc38-9d5548077fe7",
        "minority": "af482991-ee6c-4180-8782-57f667a55919",
        "compact": "530f41fb-d39f-492a-9028-8886bd499eed",
        "splitting": "d26ec0e1-f53a-4ebd-9aa8-7e18accb04af",
    },
    "MA": {
        "proportional": "9cf86106-cfc2-402d-9365-8206ef77f6ee",
        "competitive": "7cda7048-7362-4543-998a-2c1b89de88a8",
        "minority": "6fdf3a89-1b63-4856-bcbb-d777b01f51a2",
        "compact": "ff5a5d69-1c81-4ce2-927b-ddb010968b33",
        "splitting": "6e745232-b017-47de-b20a-09de51e720f1",
    },
    "MI": {
        "proportional": "4c1a46f3-3eed-4b0b-9f1e-74e1e1c63a97",
        "competitive": "fd5de4ef-5069-4aa3-987e-0c4faa50f9d9",
        "minority": "2d2c9c5a-8812-408b-9343-36317052bd95",
        "compact": "6a943e97-c4d7-4111-939a-6eef1fb652d8",
        "splitting": "b0c02efc-6507-4e73-93c2-1ced3d8d469f",
    },
    "MN": {
        "proportional": "e96c7448-d5ba-4500-b158-06f2ff6e1453",
        "competitive": "7e2f65af-b848-4ecc-83d3-f0e958b9406f",
        "minority": "fcfc1a01-7ad3-46c3-a3e6-41222ea0cf48",
        "compact": "64858a6b-6511-4f16-834f-776ab91205e0",
        "splitting": "1d7a0cc7-7199-42a8-805d-8f7e14c60d6e",
    },
    "MS": {
        "proportional": "78f2536f-c30f-41f0-ace3-d0f2597f7c27",
        "competitive": "e7be9ef9-d9ff-42ca-8e04-3226b3b413d8",
        "minority": "cf2ebd05-d118-4ecf-a8f4-824c6cb6ba67",
        "compact": "9e1d67b8-162c-4c44-b15a-263d3ae6f026",
        "splitting": "35c56e88-6ac3-4f3e-b732-7e37221395c7",
    },
    "MO": {
        "proportional": "a39beb81-f839-4755-a35f-05bc79ee68a0",
        "competitive": "f07502f1-f94d-47c6-b083-f41aadb0f7ee",  # copy of "127dfd4d-094a-4cdc-ac9e-e98829a664dc"
        # "competitive": "a110a70b-d083-4934-905c-2ba0dae7256f",
        "minority": "d1ce2e50-1c28-4aae-a95e-71b1ab361c8a",
        "compact": "9cc3d9c3-44c6-4a62-8db9-7846ac12688f",
        "splitting": "abc98af0-3ef8-4861-96cc-40f7173d9d14",
    },
    "NE": {
        "proportional": "a2d83af8-8aab-492f-9f10-9be4b9a263f1",
        "competitive": "adacc8ce-05c6-4d86-8fb3-99d0ace9f25d",
        "minority": "eb4be8c9-3ea4-494f-a98d-226f597bd5da",
        "compact": "f7720b75-58d6-4e2d-bff0-894e2c7b5f41",
        "splitting": "4ff0b106-818d-4f7a-987a-39205bdcb008",
    },
    "NV": {
        "proportional": "c9b38b70-d05a-4d6f-b6ec-f237da8ca34f",
        "competitive": "3ac3a189-ea62-4d90-baec-6e7e46c9893d",
        "minority": "387a0b00-171b-4821-8479-63bcdaf2d79a",  # a copy of cd1c643b-7353-4d8e-b9ab-072ef603508d
        "compact": "8da2d779-b8bd-4e27-bae7-340fa87a4376",
        "splitting": "baa3cfad-e4f8-452c-9c5d-a71bd4efd9ff",
    },
    "NJ": {
        "proportional": "5cb13428-1e13-4e5e-b4ab-547478caed4b",
        "competitive": "3c54c696-ae75-4eda-a260-5a95a2c276ef",
        "minority": "ddc291dc-1f0b-4b88-b57a-ff410c75af81",
        "compact": "f254884d-267e-43b4-9d7e-2d9812c13788",
        "splitting": "a3afe5ca-4430-483f-82ca-39922fa5d3dc",
    },
    "NM": {
        "proportional": "2051bf23-0195-4d89-aceb-252d78c32dc4",  # copy of "3cab7943-cc5d-4c56-a460-307ca987324a"
        # "proportional": "1739a3fd-0a61-40b4-affe-2d9943568477",
        "competitive": "57893e66-fd7d-464a-8e6f-c39b69609b73",  # copy of "0852f3ca-438e-43be-858c-72e6fd797f98"
        # "competitive": "2e487b62-e26b-4c96-92de-0ffd20feade6",
        "minority": "46afff6c-1f2c-43bb-bfeb-1c69f75fa403",  # copy of "3cab7943-cc5d-4c56-a460-307ca987324a"
        # "minority": "5dcbf4ee-ad06-4fb2-9d30-45b7b1496a3f",
        "compact": "769b245f-4c5d-4a93-98a5-6cd2e66420a2",  # copy of "e7ac5c2a-ce36-4780-ab04-0fc82faac874"
        # "compact": "a569b54b-eebb-42c7-af2a-373d13142d05",
        "splitting": "cd28107e-5ede-4f74-bbf5-dae7f54c17e3",
    },
    "NY": {
        "proportional": "65aaf6b6-2abf-4f2f-9313-7fb0c32aca2c",
        "competitive": "48987808-7ab5-4846-b281-54f58bd24d67",
        "minority": "20775253-b960-4542-8a7b-165635b006cc",
        "compact": "6d9a1e16-c5d2-48a0-80f1-d06fe6d56b7f",
        "splitting": "149fe85d-04c2-4d11-b959-98fe52f1772b",
    },
    "NC": {
        "proportional": "eb89e54f-69aa-4742-90e9-83b696871348",
        "competitive": "3ba3e193-414c-4a17-a9ef-57b326ede3d9",
        "minority": "565513d2-f7e5-492f-81f7-7cd10c054a18",
        "compact": "c9ed708a-3c2f-4b29-b55e-3bbfda14db7f",
        "splitting": "fbbde7c8-f8e6-47ff-ae18-8307f344a8f6",
    },
    "OH": {
        "proportional": "43ac2051-66af-46d4-817f-3fca031b4008",
        "competitive": "e7043d87-a24a-41fd-b3e3-f4a1162548a7",
        "minority": "b95bb90a-426f-40a0-a06d-d3027e646617",
        "compact": "486a1fd0-f56e-435b-8e69-a080e99fe58d",
        "splitting": "5c6e887d-49a8-426f-8b7b-5f3400cc62a1",
    },
    "OK": {
        "proportional": "2943140f-a1bd-45c1-a455-dc14c5393eed",
        "competitive": "ca3b3e26-9a73-422f-a40c-cd7b240e053d",  # copy of "2de2dd82-508d-4c6d-a626-b41373f1a9b7"
        # "competitive": "b8794457-352e-4412-9908-027f95cc9b1d",
        "minority": "9d2fa2d3-a6fa-4b65-b902-3d26e8c7b41a",
        "compact": "fbec07f7-2c67-4928-aedc-956f551aee08",  # copy of "10e4bc47-38a4-4b0d-9329-81b40bc039f4"
        # "compact": "5d052539-7560-4200-9e96-c920cda86b4f",
        "splitting": "d47c3741-ec79-48d4-8c95-f938a526cf4b",
    },
    "OR": {
        "proportional": "49749f47-8d78-4d36-a8b3-1265cd3b0191",
        "competitive": "37764638-8e2d-45d0-8322-28c4a171d71c",
        "minority": "b914939e-5e90-4e73-a51b-60e157670b24",
        "compact": "6d9ec3b7-e462-401f-ac5b-9ef37b35f32e",
        "splitting": "6a9fdbbb-01ce-4a5d-8fcb-38788646368b",
    },
    "PA": {
        "proportional": "60f36296-fdbc-420c-9094-91efbe53041e",
        "competitive": "e3c3b909-508a-4095-8c22-93ba9fc5b030",
        "minority": "17290afc-2e93-407b-af6c-c6a26d051dad",
        "compact": "e0fa7e79-26a4-4d27-8028-745a84fea1c1",
        "splitting": "dc16b2ec-4609-42ca-9ea8-02697564d52c",
    },
    "SC": {
        "proportional": "5132f119-2ca1-4b91-9c67-9517ae1824be",
        "competitive": "521725a2-3c2a-498a-bb95-0a64622b5d52",
        "minority": "206ddd70-ef2d-48ff-ba91-c7db687cb9a6",
        "compact": "bf225fbb-c06b-4a26-a00c-e98bd9344347",
        "splitting": "61d2f566-0939-4ced-8586-2c216a6b1965",
    },
    "TN": {
        "proportional": "c9ec1171-e733-41be-ae73-faadbd4f9eff",
        "competitive": "cea6a3dc-70e7-4be3-8eb2-d994a237226b",
        "minority": "c0c61d14-db2e-44db-8b81-c9f535808b3a",
        "compact": "57c3bb60-5f54-4cc1-a1b7-4942584fdc6f",
        "splitting": "512a7c6f-4dde-4773-a8b0-a933014e7982",
    },
    "TX": {
        "proportional": "5a8bcd01-5b7b-4cb0-ba97-775c127412c2",
        "competitive": "b3168e80-5ec4-49e2-b3bd-928cf2ffffdc",
        "minority": "55687012-5c38-4fc2-9b19-a6b325e5e8cb",
        "compact": "3670b0b1-7083-4d20-9cee-5c5389dfdcf4",
        "splitting": "959c211a-e7db-40fe-9703-0082de3fd50f",
    },
    "UT": {
        "proportional": "cb2cd60d-74db-41a4-bcd3-d2908033a17a",
        "competitive": "29776f42-efdb-485d-942d-9ec738756de9",
        "minority": "0c38f235-f832-43a6-b77d-98ffcc4a196f",
        "compact": "d4b7682f-e1df-40d0-9770-6d85a1176a12",
        "splitting": "a26f10a5-cfeb-4989-919c-5df3c79dcb29",
    },
    "VA": {
        "proportional": "e629d89d-0ba5-4cfb-af0d-1f5a26540847",
        "competitive": "b2e40a2b-d0c3-4394-bd6c-9a387977d577",
        "minority": "3ff32d6a-1ddc-47df-ba3f-d1004f6ec6ab",
        "compact": "30a7dba3-43b0-4815-8ccd-7abbcfcf5cfa",
        "splitting": "9bd6b5b4-f8f6-4372-a45f-77b6b1668596",
    },
    "WA": {
        "proportional": "c8ac870c-f608-4f06-a519-fca814cd87c9",
        "competitive": "ee915375-d42d-4be8-8858-18302b68e684",
        "minority": "9b6064ae-6aa8-4ea7-af3e-2e0dde3c123f",
        "compact": "5ece8404-5181-4aef-8dbf-126029f60dad",
        "splitting": "3a2a23c8-d65c-4a5b-ab4f-35ccb3eab67d",
    },
    "WI": {
        "proportional": "e2a8430d-0721-4a77-a70c-f1b39423f76f",
        "competitive": "98421457-d1bf-4036-bb54-acf3b87c93c3",
        "minority": "ab4e662f-3113-4415-b046-4a41ab2fc6e2",
        "compact": "ee9bc88a-f00a-4284-be14-a6b61b9ca203",
        "splitting": "4ad1f885-3b85-4dc7-bf36-605a122f4b13",
    },
    # States w/ 2 congressional districts
    "ID": {
        "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "competitive": "f404dcbc-4763-4405-8ee8-9de38763ab9c",
        "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "compact": "c04b3d59-ad9b-4d34-a56c-a40e4a2faaaf",
        "splitting": "0549f613-9577-4a0f-ba17-f821552e3512",
    },
    "MT": {
        "proportional": "968024a3-66d9-40fb-8503-963475d9ec3a",
        "competitive": "00899589-f1ed-47be-bed4-2977ad156b5e",
        "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "compact": "7ef9c6cc-9009-4a46-a135-b02a015e0588",
        "splitting": "a8bbd540-253e-4c9b-aa51-492925c0a896",
    },
    "NH": {
        "proportional": "9c0a775c-8886-4fcf-852a-c3cd8aad2ff5",
        "competitive": "4dc15785-8867-4a13-9c06-bb2a7ffecbb7",
        "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "compact": "7a525a0e-d481-4f1a-a3c7-380134fabd02",
        "splitting": "fddf7e78-d454-497f-b9a6-d5b5740f21d6",
    },
    "RI": {
        "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "competitive": "9b7b2ce0-e1dc-48fe-89ec-0b2298cdb8f9",
        "minority": "bd87b715-1286-4ffa-9f42-056f18693d9f",
        "compact": "56621991-7577-42cf-ae24-8b1cb8fb0587",
        "splitting": "83816f12-ddf0-4a45-a49d-a9908e2922e1",
    },
    "WV": {
        "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "competitive": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "compact": "d0785c40-b290-4c44-9f29-48f28edaf96e",
        "splitting": "0556f0d1-950d-4581-8777-67cc912d7280",
    },
}


baseline_maps: dict[str, str] = {
    # States w/ 3 or more congressional districts
    "AL": "d16848f7-22a0-41a5-b19e-719923c54ee3",  # 06/27/23
    "AR": "c82e8e31-bd27-4f10-bf28-cf92a67a6c79",  # 06/27/23
    "AZ": "82cdf840-22b9-4af7-9e5a-0c6a17c4b88c",  # 06/27/23
    "CA": "239aeac7-3a09-4d6a-98d8-3de61f890b70",  # 06/27/23
    "CO": "867ed109-5f5b-4aa7-bc21-36f5d8b122c9",  # 06/27/23
    "CT": "1dbaa1de-68f0-4547-b6e9-db81617eb904",  # 06/27/23
    "FL": "25a30adb-d32e-4f5e-a45a-42b2e08183ef",  # 06/28/23
    "GA": "a44aa7ca-8fa0-43a2-9ba2-2b7f45a3c0f0",  # 06/28/23
    "IA": "7292b0dc-4911-4878-9960-68ae3a6abc10",  # 06/28/23
    "IL": "4dd9fe52-b38b-4f63-a041-36e3cd7afde0",  # 06/28/23
    "IN": "75a78afd-46b9-427f-9410-62204c3c5939",  # 06/27/23
    "KS": "9901f45d-6169-4577-ba9b-43c2fe2893d8",  # 06/28/23
    "KY": "a3a061bc-3178-4ae6-bdf0-a525ad6639b2",  # 06/28/23
    "LA": "e59f8d73-e552-4fd3-98d0-368722302720",  # 06/27/23
    "MA": "cfc4a446-c1d1-451e-affa-a79c52ea671e",  # 06/28/23
    "MD": "f6624aac-a170-4b52-a9b4-121322b12a9a",  # 06/28/23
    "MI": "0e074091-d3a7-4a79-bec7-a6c4641db018",  # 06/28/23
    "MN": "41893bfd-df1e-49b7-9322-6c134575dd35",  # 06/28/23
    "MO": "d1fdc45c-7d5e-45f5-af95-832094008465",  # 06/28/23
    "MS": "83d7ca09-2016-4b5a-b19c-e3009726557e",  # 06/28/23
    "NC": "5e651803-4c40-4b04-a5ca-0c4e267b7036",  # 06/28/23
    "NE": "9cda0d21-d033-45d8-b901-ada2d95e4a59",  # 06/28/23
    "NJ": "b687ee33-5fae-43ce-b161-d49a1ddfab98",  # 06/28/23
    "NM": "ce4101f0-3fed-4902-88d0-170b7d0e3ca9",  # 06/28/23
    "NV": "b11b591a-94cf-475f-bb54-8f186e2cf12a",  # 06/28/23
    "NY": "bea0efc4-52e7-4bbb-b942-67637ed4ab8a",  # 06/28/23
    "OH": "82aca24a-0bf3-4e3d-abb2-ff51d934be01",  # 06/28/23
    "OK": "09062ff7-ce80-42ad-bb8d-74cb9815e974",  # 06/28/23
    "OR": "84976420-5049-4e8e-bafa-985d4a392d97",  # 06/28/23
    "PA": "34f4ae9c-c4cb-42e4-b551-841bcf4a95f1",  # 06/28/23
    "SC": "adb40672-45a8-43ba-bf72-a73bef7c98ab",  # 06/28/23
    "TN": "9a80c60b-a2ec-4696-af5e-0653039fcbaf",  # 06/28/23
    "TX": "bb716f76-f6b9-4f61-8590-451007a1190b",  # 06/28/23
    "UT": "e1d41beb-0f2f-4029-b31f-ffa1593e2d9e",  # 06/28/23
    "VA": "c7cba809-9d12-428c-b013-9b4b9f9a5a91",  # 06/28/23
    "WA": "989ac5b1-debe-4960-b7ca-d29d089c858d",  # 06/28/23
    "WI": "4d17758d-3a3b-4b62-87a9-bac8da1fd645",  # 06/28/23
    # Additional states w/ 2 congressional districts
    "ID": "e6f75d1c-4756-4ebe-99fe-9012d6777ed8",  # 07/15/23
    "MT": "62590347-4639-4f63-b505-6bb2409c66eb",  # 07/15/23
    "NH": "9309e340-f8f7-46f3-81dc-69805f9fbeca",  # 07/15/23
    "RI": "c7e73ead-eeb0-4a81-9708-caadff6428e6",  # 07/16/23
    "WV": "a0a0dbd0-e472-47c1-b3c6-e1e51219fabc",  # 07/16/23
}


### END ###

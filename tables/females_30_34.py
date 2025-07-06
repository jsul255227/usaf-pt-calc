# females_30_34.py
# Official USAF PT scoring tables for Females Age 30-34
# Template based on previous age groups. Fill in each component as official values are provided.

# Helper function: Convert 'mm:ss' string to total seconds (int)
def mmss_to_seconds(mmss):
    """
    Convert a time string in 'mm:ss' format to total seconds.
    Example: '9:13' -> 553
    """
    m, s = map(int, mmss.split(':'))
    return m * 60 + s

# ----------------------
# Cardio: 1.5 Mile Run
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Lower time = higher score.
FEMALE_30_34_RUN = [
    (0, mmss_to_seconds('10:51') - 1, 60.0),                 # < 10:51
    (mmss_to_seconds('10:52'), mmss_to_seconds('11:22'), 59.5),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 59.0),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 58.5),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 58.0),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 57.5),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 57.0),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 56.5),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 56.0),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 55.5),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 55.0),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 54.5),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 54.0),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 52.5),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 51.0),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 49.5),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 47.0),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 44.5),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 42.0),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 38.5),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 35.0), # 20:33*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
FEMALE_30_34_HAMR = [
    (78, float('inf'), 60.0),         # > 77
    (71, 77, 59.5),
    (68, 70, 59.0),
    (65, 67, 58.5),
    (62, 64, 58.0),
    (59, 61, 57.5),
    (56, 58, 57.0),
    (54, 55, 56.5),
    (51, 53, 56.0),
    (48, 50, 55.5),
    (45, 47, 55.0),
    (42, 44, 54.5),
    (39, 41, 54.0),
    (36, 38, 52.5),
    (33, 35, 51.0),
    (30, 32, 49.5),
    (27, 29, 47.0),
    (24, 26, 44.5),
    (22, 23, 42.0),
    (19, 21, 38.5),
    (16, 18, 35.0),                   # 16*-18
]

# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_30_34_PUSHUPS = [
    (47, float('inf'), 20.0),      # > 46
    (45, 46, 19.9),
    (44, 44, 19.8),
    (43, 43, 19.6),
    (42, 42, 19.4),
    (41, 41, 19.2),
    (40, 40, 19.0),
    (39, 39, 18.8),
    (38, 38, 18.7),
    (37, 37, 18.6),
    (36, 36, 18.4),
    (35, 35, 18.3),
    (34, 34, 18.2),
    (33, 33, 18.0),
    (32, 32, 17.9),
    (31, 31, 17.8),
    (30, 30, 17.6),
    (29, 29, 17.4),
    (28, 28, 17.3),
    (27, 27, 17.2),
    (26, 26, 17.0),
    (25, 25, 16.6),
    (24, 24, 16.4),
    (23, 23, 16.0),
    (22, 22, 15.8),
    (21, 21, 15.6),
    (20, 20, 15.2),
    (19, 19, 15.0),
    (18, 18, 14.0),
    (17, 17, 13.6),
    (16, 16, 13.0),
    (15, 15, 12.0),
    (14, 14, 10.0),
    (13, 13, 7.0),
    (12, 12, 4.0),
    (11, 11, 1.0),                # 11*
]

# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_30_34_HR_PUSHUPS = [
    (32, float('inf'), 20.0),      # > 31
    (30, 31, 19.6),
    (29, 29, 19.2),
    (28, 28, 18.8),
    (27, 27, 18.4),
    (26, 26, 18.0),
    (25, 25, 17.6),
    (24, 24, 17.2),
    (23, 23, 16.8),
    (22, 22, 16.4),
    (21, 21, 16.0),
    (20, 20, 15.6),
    (19, 19, 15.2),
    (18, 18, 14.8),
    (17, 17, 14.4),
    (16, 16, 14.0),
    (15, 15, 13.6),
    (14, 14, 13.2),
    (13, 13, 12.8),
    (12, 12, 12.4),
    (11, 11, 12.0),
    (10, 10, 11.6),
    (9, 9, 11.2),
    (8, 8, 10.8),
    (7, 7, 10.4),
    (6, 6, 10.0),                # 6*
]

# ----------------------
# Strength: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_30_34_SITUPS = [
    (46, float('inf'), 20.0),      # > 45
    (44, 45, 19.7),
    (43, 43, 19.4),
    (42, 42, 19.0),
    (41, 41, 18.8),
    (40, 40, 18.0),
    (39, 39, 17.6),
    (38, 38, 17.0),
    (37, 37, 16.6),
    (36, 36, 16.4),
    (35, 35, 16.0),
    (34, 34, 15.6),
    (33, 33, 15.0),
    (32, 32, 14.0),
    (31, 31, 13.6),
    (30, 30, 13.0),
    (29, 29, 12.0),
    (28, 28, 9.0),
    (27, 27, 6.0),
    (26, 26, 3.0),                # 26*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_30_34_CRUNCH = [
    (45, float('inf'), 20.0),      # > 44
    (43, 44, 19.7),
    (42, 42, 19.4),
    (41, 41, 19.1),
    (40, 40, 18.9),
    (39, 39, 18.6),
    (38, 38, 18.3),
    (37, 37, 18.0),
    (36, 36, 17.7),
    (35, 35, 17.4),
    (34, 34, 17.1),
    (33, 33, 16.9),
    (32, 32, 16.6),
    (31, 31, 16.3),
    (30, 30, 16.0),
    (29, 29, 15.7),
    (28, 28, 15.4),
    (27, 27, 15.1),
    (26, 26, 14.9),
    (25, 25, 14.6),
    (24, 24, 14.3),
    (23, 23, 14.0),
    (22, 22, 13.7),
    (21, 21, 13.4),
    (20, 20, 13.1),
    (19, 19, 12.9),
    (18, 18, 12.6),
    (17, 17, 12.3),
    (16, 16, 12.0),
    (15, 15, 11.7),
    (14, 14, 11.4),
    (13, 13, 11.1),
    (12, 12, 10.9),
    (11, 11, 10.6),
    (10, 10, 10.3),
    (9, 9, 10.0),                # 9*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
FEMALE_30_34_PLANK = [
    (mmss_to_seconds('3:21'), float('inf'), 20.0),      # > 3:20
    (mmss_to_seconds('3:15'), mmss_to_seconds('3:20'), 19.7),
    (mmss_to_seconds('3:09'), mmss_to_seconds('3:14'), 19.3),
    (mmss_to_seconds('3:02'), mmss_to_seconds('3:08'), 18.8),
    (mmss_to_seconds('2:55'), mmss_to_seconds('3:01'), 18.4),
    (mmss_to_seconds('2:35'), mmss_to_seconds('2:54'), 17.1),
    (mmss_to_seconds('2:15'), mmss_to_seconds('2:34'), 15.8),
    (mmss_to_seconds('1:55'), mmss_to_seconds('2:14'), 14.5),
    (mmss_to_seconds('1:35'), mmss_to_seconds('1:54'), 13.2),
    (mmss_to_seconds('1:15'), mmss_to_seconds('1:34'), 11.9),
    (mmss_to_seconds('0:55'), mmss_to_seconds('1:14'), 10.6),
    (mmss_to_seconds('0:50'), mmss_to_seconds('0:54'), 10.3),
    (mmss_to_seconds('0:45'), mmss_to_seconds('0:49'), 10.0), # 0:45*
]

# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------

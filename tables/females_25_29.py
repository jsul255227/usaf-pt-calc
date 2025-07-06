# females_25_29.py
# Official USAF PT scoring tables for Females Age 25-29
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
FEMALE_25_29_RUN = [
    (0, mmss_to_seconds('10:37') - 1, 60.0),                 # < 10:37
    (mmss_to_seconds('10:38'), mmss_to_seconds('11:06'), 59.5),
    (mmss_to_seconds('11:07'), mmss_to_seconds('11:22'), 59.0),
    (mmss_to_seconds('11:23'), mmss_to_seconds('11:38'), 58.5),
    (mmss_to_seconds('11:39'), mmss_to_seconds('11:56'), 58.0),
    (mmss_to_seconds('11:57'), mmss_to_seconds('12:14'), 57.5),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 57.0),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 56.5),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 56.0),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 55.5),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 55.0),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 54.5),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 54.0),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 53.5),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 52.0),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 50.5),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 49.0),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 45.5),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 42.0),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 38.5),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 35.0), # 19:43*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
FEMALE_25_29_HAMR = [
    (81, float('inf'), 60.0),         # > 80
    (74, 80, 59.5),
    (71, 73, 59.0),
    (68, 70, 58.5),
    (65, 67, 58.0),
    (62, 64, 57.5),
    (59, 61, 57.0),
    (56, 58, 56.5),
    (54, 55, 56.0),
    (51, 53, 55.5),
    (48, 50, 55.0),
    (45, 47, 54.5),
    (42, 44, 54.0),
    (39, 41, 53.5),
    (36, 38, 52.0),
    (33, 35, 50.5),
    (30, 32, 49.0),
    (27, 29, 45.5),
    (24, 26, 42.0),
    (22, 23, 38.5),
    (19, 21, 35.0),                   # 19*-21
]

# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_25_29_PUSHUPS = [
    (48, float('inf'), 20.0),      # > 47
    (46, 47, 19.8),
    (45, 45, 19.6),
    (44, 44, 19.4),
    (43, 43, 19.2),
    (42, 42, 19.0),
    (41, 41, 18.8),
    (40, 40, 18.6),
    (39, 39, 18.4),
    (38, 38, 18.2),
    (37, 37, 18.0),
    (36, 36, 17.8),
    (35, 35, 17.6),
    (34, 34, 17.2),
    (33, 33, 17.0),
    (32, 32, 16.8),
    (31, 31, 16.6),
    (30, 30, 16.4),
    (29, 29, 16.2),
    (28, 28, 16.0),
    (27, 27, 15.0),
    (26, 26, 14.6),
    (25, 25, 14.4),
    (24, 24, 14.0),
    (23, 23, 13.0),
    (22, 22, 12.6),
    (21, 21, 12.0),
    (20, 20, 11.6),
    (19, 19, 11.0),
    (18, 18, 10.6),
    (17, 17, 10.0),
    (16, 16, 7.0),
    (15, 15, 4.0),
    (14, 14, 1.0),                # 14*
]

# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_25_29_HR_PUSHUPS = [
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
FEMALE_25_29_SITUPS = [
    (51, float('inf'), 20.0),      # > 50
    (49, 50, 19.5),
    (48, 48, 19.0),
    (47, 47, 18.8),
    (46, 46, 18.0),
    (45, 45, 17.8),
    (44, 44, 17.2),
    (43, 43, 17.0),
    (42, 42, 16.0),
    (41, 41, 15.6),
    (40, 40, 15.0),
    (39, 39, 14.6),
    (38, 38, 14.0),
    (37, 37, 13.6),
    (36, 36, 13.0),
    (35, 35, 12.6),
    (34, 34, 12.0),
    (33, 33, 9.0),
    (32, 32, 6.0),
    (31, 31, 3.0),                # 31*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_25_29_CRUNCH = [
    (46, float('inf'), 20.0),      # > 45
    (44, 45, 19.7),
    (43, 43, 19.4),
    (42, 42, 19.2),
    (41, 41, 18.9),
    (40, 40, 18.6),
    (39, 39, 18.3),
    (38, 38, 18.1),
    (37, 37, 17.8),
    (36, 36, 17.5),
    (35, 35, 17.2),
    (34, 34, 16.9),
    (33, 33, 16.7),
    (32, 32, 16.4),
    (31, 31, 16.1),
    (30, 30, 15.8),
    (29, 29, 15.6),
    (28, 28, 15.3),
    (27, 27, 15.0),
    (26, 26, 14.7),
    (25, 25, 14.4),
    (24, 24, 14.2),
    (23, 23, 13.9),
    (22, 22, 13.6),
    (21, 21, 13.3),
    (20, 20, 13.1),
    (19, 19, 12.8),
    (18, 18, 12.5),
    (17, 17, 12.2),
    (16, 16, 11.9),
    (15, 15, 11.7),
    (14, 14, 11.4),
    (13, 13, 11.1),
    (12, 12, 10.8),
    (11, 11, 10.6),
    (10, 10, 10.3),
    (9, 9, 10.0),                # 9*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
FEMALE_25_29_PLANK = [
    (mmss_to_seconds('3:26'), float('inf'), 20.0),      # > 3:25
    (mmss_to_seconds('3:20'), mmss_to_seconds('3:25'), 19.8),
    (mmss_to_seconds('3:14'), mmss_to_seconds('3:19'), 19.6),
    (mmss_to_seconds('3:07'), mmss_to_seconds('3:13'), 19.3),
    (mmss_to_seconds('3:00'), mmss_to_seconds('3:06'), 19.1),
    (mmss_to_seconds('2:40'), mmss_to_seconds('2:59'), 16.9),
    (mmss_to_seconds('2:20'), mmss_to_seconds('2:39'), 16.2),
    (mmss_to_seconds('2:00'), mmss_to_seconds('2:19'), 15.5),
    (mmss_to_seconds('1:40'), mmss_to_seconds('1:59'), 13.3),
    (mmss_to_seconds('1:20'), mmss_to_seconds('1:39'), 12.5),
    (mmss_to_seconds('1:00'), mmss_to_seconds('1:19'), 11.8),
    (mmss_to_seconds('0:55'), mmss_to_seconds('0:59'), 10.2),
    (mmss_to_seconds('0:50'), mmss_to_seconds('0:54'), 10.0),   # 0:50*
]

# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------

# males_55_59.py
# Official USAF PT scoring tables for Males 55-59
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
# Cardio: 1.5 Mile Run (official July 2025)
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Lower time = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_55_59_RUN = [
    (0, mmss_to_seconds('10:51') - 1, 60.0),                 # < 10:51
    (mmss_to_seconds('10:51'), mmss_to_seconds('11:22'), 59.5),
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
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 53.5),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 52.0),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 50.5),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 48.0),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 45.5),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 43.0),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 40.5),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 38.0),
    (mmss_to_seconds('20:34'), mmss_to_seconds('21:28'), 35.0), # 21:28*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_55_59_HAMR = [
    (78, float('inf'), 60.0),         # > 77
    (71, 76, 59.5),
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
    (36, 38, 53.5),
    (33, 35, 52.0),
    (30, 32, 50.5),
    (27, 29, 48.0),
    (24, 26, 45.5),
    (22, 23, 43.0),
    (19, 21, 40.5),
    (16, 18, 38.0),
    (13, 15, 35.0),                   # 13*-15
]

# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_55_59_PUSHUPS = [
    (34, float('inf'), 20.0),      # > 33
    (32, 33, 19.8),
    (31, 31, 19.4),
    (30, 30, 19.0),
    (29, 29, 18.4),
    (28, 28, 18.0),
    (27, 27, 17.8),
    (26, 26, 17.4),
    (25, 25, 17.0),
    (24, 24, 16.8),
    (23, 23, 15.8),
    (22, 22, 14.8),
    (21, 21, 14.0),
    (20, 20, 13.0),
    (19, 19, 12.4),
    (18, 18, 11.8),
    (17, 17, 11.4),
    (16, 16, 10.8),
    (15, 15, 10.0),
    (14, 14, 7.0),
    (13, 13, 4.0),
    (12, 12, 1.0),                # 12*
]

# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_55_59_HR_PUSHUPS = [
    (34, float('inf'), 20.0),      # > 33
    (32, 33, 19.6),
    (31, 31, 19.1),
    (30, 30, 18.7),
    (29, 29, 18.3),
    (28, 28, 17.8),
    (27, 27, 17.4),
    (26, 26, 17.0),
    (25, 25, 16.5),
    (24, 24, 16.1),
    (23, 23, 15.7),
    (22, 22, 15.2),
    (21, 21, 14.8),
    (20, 20, 14.3),
    (19, 19, 13.9),
    (18, 18, 13.5),
    (17, 17, 13.0),
    (16, 16, 12.6),
    (15, 15, 12.2),
    (14, 14, 11.7),
    (13, 13, 11.3),
    (12, 12, 10.9),
    (11, 11, 10.4),
    (10, 10, 10.0),                # 10*
]

# ----------------------
# Strength: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_55_59_SITUPS = [
    (45, float('inf'), 20.0),      # > 44
    (43, 44, 19.7),
    (42, 42, 19.4),
    (41, 41, 19.0),
    (40, 40, 18.8),
    (39, 39, 18.4),
    (38, 38, 18.2),
    (37, 37, 18.0),
    (36, 36, 17.6),
    (35, 35, 17.4),
    (34, 34, 17.0),
    (33, 33, 16.0),
    (32, 32, 15.6),
    (31, 31, 15.0),
    (30, 30, 14.6),
    (29, 29, 14.0),
    (28, 28, 13.6),
    (27, 27, 13.0),
    (26, 26, 12.6),
    (25, 25, 12.0),
    (24, 24, 9.0),
    (23, 23, 6.0),
    (22, 22, 3.0),                # 22*
]

# ----------------------
# Core: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_55_59_CRUNCH = [
    (42, float('inf'), 20.0),      # > 41
    (40, 41, 19.7),
    (39, 39, 19.4),
    (38, 38, 19.1),
    (37, 37, 18.8),
    (36, 36, 18.5),
    (35, 35, 18.2),
    (34, 34, 17.9),
    (33, 33, 17.6),
    (32, 32, 17.3),
    (31, 31, 17.0),
    (30, 30, 16.7),
    (29, 29, 16.4),
    (28, 28, 16.1),
    (27, 27, 15.8),
    (26, 26, 15.5),
    (25, 25, 15.2),
    (24, 24, 14.8),
    (23, 23, 14.5),
    (22, 22, 14.2),
    (21, 21, 13.9),
    (20, 20, 13.6),
    (19, 19, 13.3),
    (18, 18, 13.0),
    (17, 17, 12.7),
    (16, 16, 12.4),
    (15, 15, 12.1),
    (14, 14, 11.8),
    (13, 13, 11.5),
    (12, 12, 11.2),
    (11, 11, 10.9),
    (10, 10, 10.6),
    (9, 9, 10.3),
    (8, 8, 10.0),                # 8*
]

# ----------------------
# Core: Forearm Plank
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
# Updated to match official USAF PT table (July 2025)
MALE_55_59_PLANK = [
    (mmss_to_seconds('3:01'), float('inf'), 20.0),   # > 3:00
    (mmss_to_seconds('2:55'), mmss_to_seconds('3:00'), 19.7),
    (mmss_to_seconds('2:50'), mmss_to_seconds('2:54'), 19.3),
    (mmss_to_seconds('2:44'), mmss_to_seconds('2:49'), 18.9),
    (mmss_to_seconds('2:37'), mmss_to_seconds('2:43'), 18.5),
    (mmss_to_seconds('2:30'), mmss_to_seconds('2:36'), 18.0),
    (mmss_to_seconds('2:10'), mmss_to_seconds('2:29'), 16.7),
    (mmss_to_seconds('1:50'), mmss_to_seconds('2:09'), 15.3),
    (mmss_to_seconds('1:30'), mmss_to_seconds('1:49'), 14.0),
    (mmss_to_seconds('1:10'), mmss_to_seconds('1:29'), 12.7),
    (mmss_to_seconds('0:50'), mmss_to_seconds('1:09'), 11.3),
    (mmss_to_seconds('0:30'), mmss_to_seconds('0:49'), 10.0),   # 0:30* minimum
]

# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------

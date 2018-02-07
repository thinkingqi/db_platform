
from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class Mysql_processlist(models.Model):
    db_ip = models.CharField(max_length=80)
    db_port = models.SmallIntegerField()
    conn_id = models.CharField(max_length=30)
    user = models.CharField(max_length=32)
    host = models.CharField(max_length=64)
    db = models.CharField(max_length=64)
    command = models.CharField(max_length=16)
    time = models.IntegerField()
    state = models.CharField(null=True,max_length=64)
    info = models.TextField(null=True)
    create_time = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'mysql_processlist'

class Mysql_replication(models.Model):
    db_ip = models.CharField(max_length=80)
    db_port = models.SmallIntegerField()
    is_master = models.SmallIntegerField(default=0)
    is_slave = models.SmallIntegerField(default=0)
    read_only = models.CharField(max_length=10,null=True)
    gtid_mode = models.CharField(max_length=10,null=True)
    master_server = models.CharField(max_length=30,null=True)
    master_port = models.CharField(max_length=20,null=True)
    slave_io_run = models.CharField(max_length=20,null=True)
    slave_sql_run = models.CharField(max_length=20,null=True)
    delay = models.CharField(max_length=20,null=True)
    current_binlog_file = models.CharField(max_length=30,null=True)
    current_binlog_pos = models.CharField(max_length=30,null=True)
    master_binlog_file = models.CharField(max_length=30,null=True)
    master_binlog_pos = models.CharField(max_length=30,null=True)
    master_binlog_space = models.BigIntegerField(default=0)
    slave_sql_running_state = models.CharField(max_length=100,null=True)
    create_time = models.DateTimeField()
    class Meta:
        db_table = 'mysql_replication'
        unique_together = ("db_ip", "db_port")

class Mysql_replication_his(models.Model):
    db_ip = models.CharField(max_length=80)
    db_port = models.SmallIntegerField()
    is_master = models.SmallIntegerField(default=0)
    is_slave = models.SmallIntegerField(default=0)
    read_only = models.CharField(max_length=10,null=True)
    gtid_mode = models.CharField(max_length=10,null=True)
    master_server = models.CharField(max_length=30,null=True)
    master_port = models.CharField(max_length=20,null=True)
    slave_io_run = models.CharField(max_length=20,null=True)
    slave_sql_run = models.CharField(max_length=20,null=True)
    delay = models.CharField(max_length=20,null=True)
    current_binlog_file = models.CharField(max_length=30,null=True)
    current_binlog_pos = models.CharField(max_length=30,null=True)
    master_binlog_file = models.CharField(max_length=30,null=True)
    master_binlog_pos = models.CharField(max_length=30,null=True)
    master_binlog_space = models.BigIntegerField(default=0)
    slave_sql_running_state = models.CharField(max_length=100,null=True)
    create_time = models.DateTimeField(db_index=True)
    class Meta:
        db_table = 'mysql_replication_his'
        index_together = [["db_ip", "db_port", "create_time"], ]


class MysqlConnected(models.Model):
    db_ip = models.CharField(max_length=80)
    db_port = models.CharField(max_length=10)
    connect_server = models.CharField(max_length=100)
    connect_user = models.CharField(max_length=50, blank=True, null=True)
    connect_db = models.CharField(max_length=50, blank=True, null=True)
    connect_count = models.IntegerField()
    create_time = models.DateTimeField(db_index=True)
    class Meta:
        db_table = 'mysql_connected'
        index_together = [["db_ip", "db_port", "create_time"], ]

class MysqlStatus(models.Model):
    db_ip = models.CharField(max_length=80)
    db_port = models.CharField(max_length=10)
    connect = models.SmallIntegerField(default=0)
    role = models.CharField(max_length=30,default=-1)
    uptime = models.IntegerField(default=-1)
    version = models.CharField(max_length=50)
    max_connections = models.SmallIntegerField(default=-1)
    max_connect_errors = models.BigIntegerField(default=-1)
    open_files_limit = models.IntegerField(default=-1)
    open_files = models.SmallIntegerField(default=-1)
    table_open_cache = models.SmallIntegerField(default=-1)
    open_tables = models.SmallIntegerField(default=-1)
    max_tmp_tables = models.SmallIntegerField(default=-1)
    max_heap_table_size = models.IntegerField(default=-1)
    max_allowed_packet = models.IntegerField(default=-1)
    threads_connected = models.IntegerField(default=-1)
    threads_running = models.IntegerField(default=-1)
    threads_created = models.IntegerField(default=-1)
    threads_cached = models.IntegerField(default=-1)
    connections = models.IntegerField(default=-1)
    aborted_clients = models.IntegerField(default=-1)
    aborted_connects = models.IntegerField(default=-1)
    connections_persecond = models.SmallIntegerField(default=-1)
    bytes_received_persecond = models.IntegerField(default=-1)
    bytes_sent_persecond = models.IntegerField(default=-1)
    com_select_persecond = models.SmallIntegerField(default=-1)
    com_insert_persecond = models.SmallIntegerField(default=-1)
    com_update_persecond = models.SmallIntegerField(default=-1)
    com_delete_persecond = models.SmallIntegerField(default=-1)
    com_commit_persecond = models.SmallIntegerField(default=-1)
    com_rollback_persecond = models.SmallIntegerField(default=-1)
    questions_persecond = models.IntegerField(default=-1)
    queries_persecond = models.IntegerField(default=-1)
    transaction_persecond = models.SmallIntegerField(default=-1)
    created_tmp_tables_persecond = models.SmallIntegerField(default=-1)
    created_tmp_disk_tables_persecond = models.SmallIntegerField(default=-1)
    created_tmp_files_persecond = models.SmallIntegerField(default=-1)
    table_locks_immediate_persecond = models.IntegerField(default=-1)
    table_locks_waited_persecond = models.SmallIntegerField(default=-1)
    key_buffer_size = models.BigIntegerField(default=-1)
    sort_buffer_size = models.IntegerField(default=-1)
    join_buffer_size = models.IntegerField(default=-1)
    key_blocks_not_flushed = models.IntegerField(default=-1)
    key_blocks_unused = models.IntegerField(default=-1)
    key_blocks_used = models.IntegerField(default=-1)
    key_read_requests_persecond = models.IntegerField(default=-1)
    key_reads_persecond = models.IntegerField(default=-1)
    key_write_requests_persecond = models.IntegerField(default=-1)
    key_writes_persecond = models.IntegerField(default=-1)
    innodb_version = models.CharField(max_length=30,default='-1')
    innodb_buffer_pool_instances = models.SmallIntegerField(default=-1)
    innodb_buffer_pool_size = models.BigIntegerField(default=-1)
    innodb_doublewrite = models.CharField(max_length=10,default='-1')
    innodb_file_per_table = models.CharField(max_length=10,default='-1')
    innodb_flush_log_at_trx_commit = models.IntegerField(default=-1)
    innodb_flush_method = models.CharField(max_length=30,default='-1')
    innodb_force_recovery = models.IntegerField(default=-1)
    innodb_io_capacity = models.IntegerField(default=-1)
    innodb_read_io_threads = models.IntegerField(default=-1)
    innodb_write_io_threads = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_total = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_data = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_dirty = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_flushed = models.BigIntegerField(default=-1)
    innodb_buffer_pool_pages_free = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_misc = models.IntegerField(default=-1)
    innodb_page_size = models.IntegerField(default=-1)
    innodb_pages_created = models.BigIntegerField(default=-1)
    innodb_pages_read = models.BigIntegerField(default=-1)
    innodb_pages_written = models.BigIntegerField(default=-1)
    innodb_row_lock_current_waits = models.CharField(max_length=100)
    innodb_buffer_pool_pages_flushed_persecond = models.IntegerField(default=-1)
    innodb_buffer_pool_read_requests_persecond = models.IntegerField(default=-1)
    innodb_buffer_pool_reads_persecond = models.IntegerField(default=-1)
    innodb_buffer_pool_write_requests_persecond = models.IntegerField(default=-1)
    innodb_rows_read_persecond = models.IntegerField(default=-1)
    innodb_rows_inserted_persecond = models.IntegerField(default=-1)
    innodb_rows_updated_persecond = models.IntegerField(default=-1)
    innodb_rows_deleted_persecond = models.IntegerField(default=-1)
    query_cache_hitrate = models.CharField(max_length=10,default='-1')
    thread_cache_hitrate = models.CharField(max_length=10,default='-1')
    key_buffer_read_rate = models.CharField(max_length=10,default='-1')
    key_buffer_write_rate = models.CharField(max_length=10,default='-1')
    key_blocks_used_rate = models.CharField(max_length=10,default='-1')
    created_tmp_disk_tables_rate = models.CharField(max_length=10,default='-1')
    connections_usage_rate = models.CharField(max_length=10,default='-1')
    open_files_usage_rate = models.CharField(max_length=10,default='-1')
    open_tables_usage_rate = models.CharField(max_length=10,default='-1')
    create_time = models.DateTimeField()
    class Meta:
        db_table = 'mysql_status'
        unique_together = ("db_ip", "db_port")

class MysqlStatusHis(models.Model):
    db_ip = models.CharField(max_length=80)
    db_port = models.CharField(max_length=10)
    connect = models.SmallIntegerField(default=0)
    role = models.CharField(max_length=30,default=-1)
    uptime = models.IntegerField(default=-1)
    version = models.CharField(max_length=50)
    max_connections = models.SmallIntegerField(default=-1)
    max_connect_errors = models.BigIntegerField(default=-1)
    open_files_limit = models.IntegerField(default=-1)
    open_files = models.SmallIntegerField(default=-1)
    table_open_cache = models.SmallIntegerField(default=-1)
    open_tables = models.SmallIntegerField(default=-1)
    max_tmp_tables = models.SmallIntegerField(default=-1)
    max_heap_table_size = models.IntegerField(default=-1)
    max_allowed_packet = models.IntegerField(default=-1)
    threads_connected = models.IntegerField(default=-1)
    threads_running = models.IntegerField(default=-1)
    # threads_waits = models.IntegerField(blank=True, null=True,default=-1)
    threads_created = models.IntegerField(default=-1)
    threads_cached = models.IntegerField(default=-1)
    connections = models.IntegerField(default=-1)
    aborted_clients = models.IntegerField(default=-1)
    aborted_connects = models.IntegerField(default=-1)
    connections_persecond = models.SmallIntegerField(default=-1)
    bytes_received_persecond = models.IntegerField(default=-1)
    bytes_sent_persecond = models.IntegerField(default=-1)
    com_select_persecond = models.SmallIntegerField(default=-1)
    com_insert_persecond = models.SmallIntegerField(default=-1)
    com_update_persecond = models.SmallIntegerField(default=-1)
    com_delete_persecond = models.SmallIntegerField(default=-1)
    com_commit_persecond = models.SmallIntegerField(default=-1)
    com_rollback_persecond = models.SmallIntegerField(default=-1)
    questions_persecond = models.IntegerField(default=-1)
    queries_persecond = models.IntegerField(default=-1)
    transaction_persecond = models.SmallIntegerField(default=-1)
    created_tmp_tables_persecond = models.SmallIntegerField(default=-1)
    created_tmp_disk_tables_persecond = models.SmallIntegerField(default=-1)
    created_tmp_files_persecond = models.SmallIntegerField(default=-1)
    table_locks_immediate_persecond = models.IntegerField(default=-1)
    table_locks_waited_persecond = models.SmallIntegerField(default=-1)
    key_buffer_size = models.BigIntegerField(default=-1)
    sort_buffer_size = models.IntegerField(default=-1)
    join_buffer_size = models.IntegerField(default=-1)
    key_blocks_not_flushed = models.IntegerField(default=-1)
    key_blocks_unused = models.IntegerField(default=-1)
    key_blocks_used = models.IntegerField(default=-1)
    key_read_requests_persecond = models.IntegerField(default=-1)
    key_reads_persecond = models.IntegerField(default=-1)
    key_write_requests_persecond = models.IntegerField(default=-1)
    key_writes_persecond = models.IntegerField(default=-1)
    innodb_version = models.CharField(max_length=30,default='-1')
    innodb_buffer_pool_instances = models.SmallIntegerField(default=-1)
    innodb_buffer_pool_size = models.BigIntegerField(default=-1)
    innodb_doublewrite = models.CharField(max_length=10,default='-1')
    innodb_file_per_table = models.CharField(max_length=10,default='-1')
    innodb_flush_log_at_trx_commit = models.IntegerField(default=-1)
    innodb_flush_method = models.CharField(max_length=30,default='-1')
    innodb_force_recovery = models.IntegerField(default=-1)
    innodb_io_capacity = models.IntegerField(default=-1)
    innodb_read_io_threads = models.IntegerField(default=-1)
    innodb_write_io_threads = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_total = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_data = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_dirty = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_flushed = models.BigIntegerField(default=-1)
    innodb_buffer_pool_pages_free = models.IntegerField(default=-1)
    innodb_buffer_pool_pages_misc = models.IntegerField(default=-1)
    innodb_page_size = models.IntegerField(default=-1)
    innodb_pages_created = models.BigIntegerField(default=-1)
    innodb_pages_read = models.BigIntegerField(default=-1)
    innodb_pages_written = models.BigIntegerField(default=-1)
    innodb_row_lock_current_waits = models.CharField(max_length=100)
    innodb_buffer_pool_pages_flushed_persecond = models.IntegerField(default=-1)
    innodb_buffer_pool_read_requests_persecond = models.IntegerField(default=-1)
    innodb_buffer_pool_reads_persecond = models.IntegerField(default=-1)
    innodb_buffer_pool_write_requests_persecond = models.IntegerField(default=-1)
    innodb_rows_read_persecond = models.IntegerField(default=-1)
    innodb_rows_inserted_persecond = models.IntegerField(default=-1)
    innodb_rows_updated_persecond = models.IntegerField(default=-1)
    innodb_rows_deleted_persecond = models.IntegerField(default=-1)
    query_cache_hitrate = models.CharField(max_length=10,default='-1')
    thread_cache_hitrate = models.CharField(max_length=10,default='-1')
    key_buffer_read_rate = models.CharField(max_length=10,default='-1')
    key_buffer_write_rate = models.CharField(max_length=10,default='-1')
    key_blocks_used_rate = models.CharField(max_length=10,default='-1')
    created_tmp_disk_tables_rate = models.CharField(max_length=10,default='-1')
    connections_usage_rate = models.CharField(max_length=10,default='-1')
    open_files_usage_rate = models.CharField(max_length=10,default='-1')
    open_tables_usage_rate = models.CharField(max_length=10,default='-1')
    create_time = models.DateTimeField(db_index=True)
    class Meta:
        db_table = 'mysql_status_his'
        index_together = [["db_ip", "db_port", "create_time"], ]


# active sql,long sql,slave delay,slave stop,connections
class Alarm(models.Model):
    db_ip = models.CharField(max_length=80)
    db_port = models.CharField(max_length=10)
    alarm_type = models.CharField(max_length=30)
    send_mail =models.SmallIntegerField(default=0)
    create_time = models.DateTimeField(db_index=True,default=timezone.now)
    class Meta:
        db_table = 'alarm'
        index_together = [["db_ip", "db_port"], ]


class AlarmTemp(models.Model):
    db_ip = models.CharField(max_length=80)
    db_port = models.CharField(max_length=10)
    alarm_type = models.CharField(max_length=30)
    create_time = models.DateTimeField(db_index=True,default=timezone.now)
    class Meta:
        db_table = 'alarm_temp'
        index_together = [["db_ip", "db_port","alarm_type"], ]